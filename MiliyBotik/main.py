import asyncio
import logging
from datetime import datetime
from html import escape

from aiogram import Bot, Dispatcher, F, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (CallbackQuery, FSInputFile, InlineKeyboardButton,
                           InlineKeyboardMarkup, KeyboardButton, Message, ReplyKeyboardMarkup)

from config import TOKEN, USERS
from html_generator import generate_html
from storage import (bind_user, create_invitation, get_invitation, get_partner,
                     get_user_id, history, nearest_invitation, set_response)

router = Router()


class DateForm(StatesGroup):
    when = State()
    place = State()
    dress_code = State()
    hint = State()
    bring = State()
    message = State()
    preview = State()


MENU = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='💌 Создать приглашение')],
    [KeyboardButton(text='💗 Ближайшее приглашение')],
    [KeyboardButton(text='📖 История свиданий')],
], resize_keyboard=True)
CANCEL = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='❌ Отмена')]], resize_keyboard=True)


def username_of(user) -> str | None:
    username = (user.username or "").lower().lstrip("@")

    print("====== ПРОВЕРКА ПОЛЬЗОВАТЕЛЯ ======")
    print("Username:", username)
    print("Telegram ID:", user.id)
    print("Разрешённые:", list(USERS.keys()))

    if username not in USERS:
        print("ОШИБКА: username не найден в USERS")
        return None

    if not bind_user(username, user.id):
        print("ОШИБКА: Telegram ID не прошёл проверку")
        return None

    print("ДОСТУП РАЗРЕШЁН")
    return username


def preview_text(inv: dict) -> str:
    when = datetime.fromisoformat(inv['datetime']).strftime('%d.%m.%Y в %H:%M')
    h = lambda name: escape(str(inv[name]))
    return (f'💌 <b>Приглашение на свидание</b>\n\n'
            f'📅 <b>Когда:</b> {when}\n'
            f'📍 <b>Место:</b> {h("place")}\n'
            f'👗 <b>Во что одеться:</b> {h("dress_code")}\n'
            f'🎒 <b>Что взять:</b> {h("bring")}\n'
            f'✨ <b>Подсказка:</b> {h("hint")}\n\n'
            f'💖 <i>{h("message")}</i>')


def invite_keyboard(inv: dict) -> InlineKeyboardMarkup:
    buttons = []
    if inv['status'] == 'pending':
        buttons.append([
            InlineKeyboardButton(text='💗 Я приду', callback_data=f'answer:accepted:{inv["id"]}'),
            InlineKeyboardButton(text='😢 Не смогу', callback_data=f'answer:declined:{inv["id"]}'),
        ])
    buttons.append([InlineKeyboardButton(text='💌 HTML-открытка', callback_data=f'html:{inv["id"]}')])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.clear()
    username = username_of(message.from_user)
    if not username or message.chat.type != 'private':
        await message.answer('🔒 Это приватный бот только для двоих.')
        return
    await message.answer(f'Привет, {USERS[username]}! 💕\nЧто будем делать?', reply_markup=MENU)


@router.message(Command('cancel'))
@router.message(F.text == '❌ Отмена')
async def cancel(message: Message, state: FSMContext):
    if not username_of(message.from_user):
        await message.answer('🔒 Доступ закрыт.')
        return
    await state.clear()
    await message.answer('Хорошо, отменили 💕', reply_markup=MENU)


@router.message(F.text == '💌 Создать приглашение')
async def begin(message: Message, state: FSMContext):
    if not username_of(message.from_user) or message.chat.type != 'private':
        await message.answer('🔒 Доступ закрыт.')
        return
    await state.clear()
    await state.set_state(DateForm.when)
    await message.answer('📅 Когда встречаемся?\nВведи дату и время: <b>25.10.2026 18:30</b>', reply_markup=CANCEL)


@router.message(DateForm.when)
async def form_when(message: Message, state: FSMContext):
    if not username_of(message.from_user):
        return
    try:
        dt = datetime.strptime(message.text or '', '%d.%m.%Y %H:%M')
        if dt <= datetime.now():
            raise ValueError
    except ValueError:
        await message.answer('Нужна будущая дата в формате <b>25.10.2026 18:30</b> 💕')
        return
    await state.update_data(datetime=dt.isoformat(timespec='minutes'))
    await state.set_state(DateForm.place)
    await message.answer('📍 Где встречаемся?')


@router.message(DateForm.place)
async def form_place(message: Message, state: FSMContext):
    await accept_field(message, state, 'place', DateForm.dress_code, '👗 Во что одеться?')


@router.message(DateForm.dress_code)
async def form_dress(message: Message, state: FSMContext):
    await accept_field(message, state, 'dress_code', DateForm.hint, '✨ Дай маленькую подсказку о свидании:')


@router.message(DateForm.hint)
async def form_hint(message: Message, state: FSMContext):
    await accept_field(message, state, 'hint', DateForm.bring, '🎒 Что взять с собой?')


@router.message(DateForm.bring)
async def form_bring(message: Message, state: FSMContext):
    await accept_field(message, state, 'bring', DateForm.message, '💌 Добавь личное сообщение:')


async def accept_field(message: Message, state: FSMContext, key: str, next_state: State, prompt: str):
    if not username_of(message.from_user):
        return
    if not message.text or not message.text.strip() or len(message.text) > 500:
        await message.answer('Напиши текст длиной от 1 до 500 символов 💕')
        return
    await state.update_data(**{key: message.text.strip()})
    await state.set_state(next_state)
    await message.answer(prompt)


@router.message(DateForm.message)
async def form_message(message: Message, state: FSMContext):
    if not username_of(message.from_user):
        return
    if not message.text or not message.text.strip() or len(message.text) > 500:
        await message.answer('Напиши текст длиной от 1 до 500 символов 💕')
        return
    await state.update_data(message=message.text.strip())
    await state.set_state(DateForm.preview)
    data = await state.get_data()
    keys = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='✅ Опубликовать', callback_data='publish')],
        [InlineKeyboardButton(text='🔄 Заполнить заново', callback_data='restart')],
    ])
    await message.answer('Вот что получилось! ✨\n\n' + preview_text(data), reply_markup=MENU)
    await message.answer('Всё правильно?', reply_markup=keys)


@router.callback_query(F.data == 'restart')
async def restart(callback: CallbackQuery, state: FSMContext):
    if not username_of(callback.from_user):
        await callback.answer('Нет доступа', show_alert=True)
        return
    if await state.get_state() != DateForm.preview.state:
        await callback.answer('Это действие уже недоступно', show_alert=True)
        return
    await state.clear()
    await state.set_state(DateForm.when)
    await callback.answer()
    await callback.message.answer('📅 Введи новую дату и время: <b>25.10.2026 18:30</b>', reply_markup=CANCEL)


@router.callback_query(F.data == 'publish')
async def publish(callback: CallbackQuery, state: FSMContext, bot: Bot):
    username = username_of(callback.from_user)
    if not username:
        await callback.answer('Нет доступа', show_alert=True)
        return
    if await state.get_state() != DateForm.preview.state:
        await callback.answer('Приглашение уже опубликовано или отменено.', show_alert=True)
        return
    details = await state.get_data()
    if datetime.fromisoformat(details['datetime']) <= datetime.now():
        await callback.answer('Дата уже прошла. Создай новое приглашение.', show_alert=True)
        return
    partner = get_partner(username, USERS)
    inv = create_invitation(username, partner, details)
    await state.clear()
    await callback.answer('Опубликовано! 💕')
    await callback.message.answer('💖 Приглашение сохранено! Ожидаем ответа.', reply_markup=MENU)
    recipient_id = get_user_id(partner)
    if recipient_id:
        try:
            await bot.send_message(recipient_id, '💌 Для тебя приготовили приглашение!\nОткрой «💗 Ближайшее приглашение».')
        except Exception:
            logging.exception('Не удалось уведомить получателя')


@router.message(F.text == '💗 Ближайшее приглашение')
async def nearest(message: Message):
    username = username_of(message.from_user)
    if not username or message.chat.type != 'private':
        await message.answer('🔒 Доступ закрыт.')
        return
    inv = nearest_invitation(username)
    if not inv:
        await message.answer('Пока нет будущих приглашений для тебя 💕', reply_markup=MENU)
        return
    status = {'pending': '⏳ Ожидает ответа', 'accepted': '✅ Ты принял(а) приглашение'}[inv['status']]
    await message.answer(preview_text(inv) + '\n\n' + status, reply_markup=invite_keyboard(inv))


@router.callback_query(F.data.startswith('answer:'))
async def answer(callback: CallbackQuery, bot: Bot):
    username = username_of(callback.from_user)
    if not username:
        await callback.answer('Нет доступа', show_alert=True)
        return
    try:
        _, status, id_text = callback.data.split(':')
        inv_id = int(id_text)
    except (ValueError, AttributeError):
        await callback.answer('Некорректная команда', show_alert=True)
        return
    inv = set_response(inv_id, username, status)
    if not inv:
        await callback.answer('Приглашение уже обработано или не твоё.', show_alert=True)
        return
    label = '💗 Приглашение принято!' if status == 'accepted' else '😢 Ответ сохранён: не смогу.'
    await callback.answer(label)
    await callback.message.answer(label, reply_markup=MENU)
    await callback.message.edit_reply_markup(reply_markup=invite_keyboard(inv))
    creator_id = get_user_id(inv['creator'])
    if creator_id:
        try:
            response = '💗 Согласие!' if status == 'accepted' else '😢 К сожалению, отказ.'
            await bot.send_message(creator_id, f'Ответ на приглашение №{inv_id}: {response}')
        except Exception:
            logging.exception('Не удалось уведомить автора')


@router.callback_query(F.data.startswith('html:'))
async def html_card(callback: CallbackQuery):
    username = username_of(callback.from_user)
    if not username:
        await callback.answer('Нет доступа', show_alert=True)
        return
    try:
        inv_id = int(callback.data.split(':')[1])
    except (ValueError, IndexError):
        await callback.answer('Некорректная команда', show_alert=True)
        return
    inv = get_invitation(inv_id)
    if inv is None or username not in (inv['creator'], inv['recipient']):
        await callback.answer('Приглашение не найдено', show_alert=True)
        return
    await callback.answer()
    path = generate_html(inv)
    await callback.message.answer_document(FSInputFile(path), caption='💌 Твоя открытка. Открой HTML-файл в браузере 💕')


@router.message(F.text == '📖 История свиданий')
async def show_history(message: Message):
    username = username_of(message.from_user)
    if not username or message.chat.type != 'private':
        await message.answer('🔒 Доступ закрыт.')
        return
    items = history(username)
    if not items:
        await message.answer('История пока пуста. Создадим первое свидание? 💗')
        return
    statuses = {'pending': '⏳', 'accepted': '💗', 'declined': '😢'}
    lines = [f'{statuses.get(i["status"], "💌")} №{i["id"]} — {datetime.fromisoformat(i["datetime"]).strftime("%d.%m.%Y %H:%M")} — {escape(i["place"][:45])}' for i in items[:15]]
    await message.answer('📖 <b>Наша история</b>\n\n' + '\n'.join(lines))


@router.message(DateForm.preview)
async def preview_note(message: Message):
    if username_of(message.from_user):
        await message.answer('Нажми «✅ Опубликовать» или «🔄 Заполнить заново» под предпросмотром.')


@router.message()
async def fallback(message: Message):
    if not username_of(message.from_user) or message.chat.type != 'private':
        await message.answer('🔒 Это приватный бот только для двоих.')
        return
    await message.answer('Выбери действие в меню 💕', reply_markup=MENU)


async def main():
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
