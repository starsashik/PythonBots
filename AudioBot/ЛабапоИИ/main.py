import datetime
import sys
import webbrowser
import pyttsx3
import speech_recognition as sr

def talk(words):
    """Произнесение текста с созданием нового движка каждый раз"""
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.5)

        # Настройка голоса
        voices = engine.getProperty('voices')
        for voice in voices:
            if 'Tatyana' in voice.name:
                engine.setProperty('voice', voice.id)
                break

        engine.say(words)
        engine.runAndWait()
        engine.stop()  # явно останавливаем движок
        del engine  # освобождаем память
    except Exception as e:
        print(f"Ошибка воспроизведения: {e}")


def command():
    r = sr.Recognizer()
    while True:  # Используем цикл вместо рекурсии
        try:
            with sr.Microphone() as source:
                print("Говорите!")
                talk("Говорите!")
                r.pause_threshold = 0.5
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)

            zadanie = r.recognize_google(audio, language="ru-RU").lower()
            print("Вы сказали: " + zadanie)
            talk("Вы сказали... " + zadanie)
            return zadanie

        except sr.UnknownValueError:
            print("Не понимаю Вас!")
            talk("Не понимаю Вас! Пожалуйста, повторите.")


def time_to_text():  # перевод времени в текст
    dict_hours = {1: 'час', 2: 'часа', 3: 'часа', 4: 'часа', 5: 'часов', 6: 'часов',
                  7: 'часов', 8: 'часов', 9: 'часов', 10: 'часов', 11: 'часов', 12: 'часов',
                  13: 'часов', 14: 'часов', 15: 'часов', 16: 'часов', 17: 'часов', 18: 'часов',
                  19: 'часов', 20: 'часов', 21: 'час', 22: 'часа', 23: 'часа', 0: 'часов'}
    dict_minutes = {
        'минута': [1, 21, 31, 41, 51],
        'минуты': [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54],
        'минут': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                  25, 26, 27, 28, 29, 30,
                  35, 36, 37, 38, 39, 40,
                  45, 46, 47, 48, 49, 50,
                  55, 56, 57, 58, 59]}

    now = datetime.datetime.now()
    h = now.hour
    m = now.minute

    str_time = str(h) + dict_hours[h] + ' ... '

    for minutes in dict_minutes:
        if m in dict_minutes[minutes]:
            str_time += str(m) + ' ' + minutes
            break

    return str_time


def ParseZadanie(zadanie):
    """Разбор голосового задания/команды"""
    if not zadanie:
        return

    if 'открой методичку' in zadanie:
        talk('Хорошо, открываю методическое пособие!')
        webbrowser.open('https://online.mospolytech.ru/mod/page/view.php?id=302613')
    elif any(phrase in zadanie for phrase in ['сколько времени', 'который час', 'сколько время']):
        talk(time_to_text())
    elif any(phrase in zadanie for phrase in ['как тебя зовут', 'как твоё имя', 'кто ты']):
        talk('Меня зовут бот Александр!')
    elif 'стоп' in zadanie or 'выход' in zadanie or 'пока' in zadanie:
        talk('Хорошо, заканчиваем разговор... До встречи!')
        sys.exit()
    else:
        talk("Я не понял команду. Попробуйте еще раз.")


if __name__ == '__main__':
    try:
        talk('Привет, меня зовут Александр! Давай поговорим!')

        while True:
            ParseZadanie(command())
            talk("Поговорим еще?")

    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем")
        talk("До свидания!")
    except Exception as e:
        print(f"Критическая ошибка: {e}")
        talk("Произошла критическая ошибка. Программа завершает работу.")
