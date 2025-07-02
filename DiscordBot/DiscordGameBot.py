# импортируем нужные нам библиотеки
import asyncio
import random
import sqlite3
from datetime import datetime
from pprint import pprint

import discord
import pymorphy2
import requests
from discord.ext import commands
from wikipedia import wikipedia

##########################################################
# важные названия (ключи, токены, ссылки, api, база данных)


db_name = "Bot.db"
BOT_TOKEN = "ODI2MDc5NzM2MjU3NTc3MDIy.GBauxC.zViZm_ggRQm6Xdvz38nppeULwRUAnokuQLIWPY"
# WEATHER_URL = "https://api.weather.yandex.ru/v2/forecast/"
# WEATHER_API_KEY = "f1419c4e-141e-41df-9c0e-a692af8b48c1"
GEOCODER_URL = "http://geocode-maps.yandex.ru/1.x/"
GEOCODER_API_KEY = "40d1649f-0493-4b70-98ba-98533de7710b"
map_api_server = "http://static-maps.yandex.ru/1.x/"
TRANSLATE_URL = "https://google-api31.p.rapidapi.com/translate"
GIPHY_URL = "http://api.giphy.com/v1/gifs/random"
GIPHY_API_KEY = "0RqPL06VxBzUsmccUTp3Whzz9SR2ncSA"


##########################################################
# функция для получения geocode'а о месте
def geocode(place):
    params = {"apikey": GEOCODER_API_KEY,
              "geocode": place,
              "format": "json"}
    response = requests.get(GEOCODER_URL, params=params)
    if response:
        json_response = response.json()
        if json_response["response"]["GeoObjectCollection"]["featureMember"]:
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            if toponym:
                return toponym
            else:
                return None


# функция для получения координат места
def get_coords(place):
    toponym = geocode(place)
    if toponym:
        return toponym["Point"]["pos"]


# функция для определения метро места
def Metro(coords):
    geocoder_request = f"https://geocode-maps.yandex.ru/1.x/?apikey={GEOCODER_API_KEY}&geocode={coords}&kind=metro&" \
                       f"results=1&format=json"
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        if json_response["response"]["GeoObjectCollection"]["featureMember"]:
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            metro = f'{toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][-1]["name"]} ' \
                    f'({toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"][-2]["name"]})'
            return metro


# функция для определения района места
def district(coords):
    geocoder_request = f"https://geocode-maps.yandex.ru/1.x/?apikey={GEOCODER_API_KEY}&geocode={coords}&kind=district&" \
                       f"results=1&format=json"
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        if json_response["response"]["GeoObjectCollection"]["featureMember"]:
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            return toponym['metaDataProperty']['GeocoderMetaData']['Address']['Components'][-2]['name']


# вспомогательная функция для перевода фразы
def translate(*txt):
    try:
        payload = {
            "text": txt,
            "to": "ru",
            "from_lang": ""
        }
        headers = {
            "x-rapidapi-key": "64aa480614msh51fdd31ab6e65aep1cdfb4jsn3f286cdf664d",
            "x-rapidapi-host": "google-api31.p.rapidapi.com",
            "Content-Type": "application/json"
        }
        response = requests.post(TRANSLATE_URL, json=payload, headers=headers)
        return response.json()[0]["translated"]
    except Exception:
        return "Ошибка :space_invader:"


##########################################################
# класс вспомогательного бота, для приветствия новых участников и самого бота
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!!", intents=discord.Intents.all())

    async def on_member_join(self, member):
        role = member.guild.get_role(834160821650718731)
        with open('data.txt', encoding='utf8') as f:
            was, dd = f.readlines()
        kolvo = int(dd)
        command = f"""SELECT wel FROM Welcome
                    WHERE id = {kolvo}"""
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        result = cur.execute(command).fetchall()
        otv = result[0][0]
        con.close()
        kolvo += 1
        if kolvo == 4:
            kolvo = 1
        with open('data.txt', mode='w', encoding='utf-8') as f1:
            f1.writelines(f'{str(was)}'
                          f'{str(kolvo)}')
        name = member.name
        otv1 = otv.replace('{member.name}', name)
        try:
            await member.add_roles(role)
        except Exception:
            pass
        await self.guilds[1].channels[5].send(f'{otv1}')

    async def on_ready(self):

        ##########################################################
        # добавляем наши вспомогательные классы в основной (раньше можно было сделать в main)
        await bot.add_cog(SanyaBot(bot))
        # await bot.add_cog(WeatherBot(bot))
        await bot.add_cog(TranslateBot(bot))
        await bot.add_cog(DateBot(bot))
        await bot.add_cog(MathBot(bot))
        await bot.add_cog(GeoBot(bot))
        await bot.add_cog(PlayBot(bot))
        ##########################################################

        with open('data.txt', encoding='utf8') as f:
            was, dd = f.readlines()
            was = int(was)
        now = datetime.now().hour * 3600 + datetime.now().minute * 60 + datetime.now().second
        if abs(now - was) >= 1800:
            await self.guilds[1].channels[5].send("""Привет, я - бот-помощник Саня, созданный исключительно в
            развлекательных целях. О моих умениях вы можете узнать, написав *!!help_bot*""")
            await self.guilds[1].channels[5].send(
                random.choice(["https://cdn.humoraf.ru/wp-content/uploads/2018/08/anime-gif-2.gif",
                               "https://media1.tenor.com/images/a477f2aa29494841f121d73a4bc30d55/tenor.gif?itemid=16945362",
                               "https://media1.tenor.com/images/730b8cb9f7c2bbece1eb9f093f5205ef/tenor.gif?itemid=5928196",
                               "https://media1.tenor.com/images/2ef78ab2f3e2acbf077388e26d3bc2da/tenor.gif?itemid=14815980",
                               "https://media1.tenor.com/images/09628191dbe81dcecc831e95a1f3e3d8/tenor.gif?itemid=7458570",
                               "https://media1.tenor.com/images/a44f316008d24797dc856c1dfd3a358d/tenor.gif?itemid=18100923",
                               "https://media1.tenor.com/images/933f8a346605b97c7e36b5cb0ae1924b/tenor.gif?itemid=17215102",
                               "https://media1.tenor.com/images/dd6393211b2201c997b3748dfcd9a659/tenor.gif?itemid=17837808",
                               "https://media1.ten  or.com/images/2e77832cba70c65df33a229118af1c8e/tenor.gif?itemid=20701760",
                               "https://media1.tenor.com/images/f82fdfe817cfb8dacb5bd5c7dadb632d/tenor.gif?itemid=8718221",
                               "https://media1.tenor.com/images/26833e994e88a08d8cb702a7253327ac/tenor.gif?itemid=19924894",
                               "https://media1.tenor.com/images/3e674bb3a6e33e2f13c7d0a415af8674/tenor.gif?itemid=15235491",
                               "https://media.tenor.com/images/9e7f5606be05a52088c3806654cecf1b/tenor.gif"]))
            with open('data.txt', mode='w', encoding='utf-8') as f1:
                f1.writelines(f'{str(now)}\n'
                              f'{str(dd)}')
        else:
            pass


# класс основного бота со всеми функциями
class SanyaBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # команда для получения помощи при работе с нащим ботом
    @commands.command(name='help_bot')
    async def helps(self, ctx):
        await ctx.send("""С помошью моих функций можно:
        Можете сыграть в игру; воспользуйтесь функцией *!!help_play*, чтобы узнать больше.
        -не работает платно- Можете узнать информацию о погоде; воспользуйтесь функцией *!!help_weather*, чтобы узнать больше.
        Можете перевести фразу на русский язык; воспользуйтесь функцией *!!help_translate*, чтобы узнать больше.
        Если вы устали, можете получить мотивацию и просто себе настроение; для этого воспользуйтесь функцией 
*!!random_advice*.
        Можете получить координаты, узнать информацию или получить спутниковое изображение любого места; 
воспользуйтесь функцией *!!help_geo*, чтобы узнать больше.
        -не работает что-то сломали не я- Можете получить ифнормацию из википедии на фразу; воспользуйтесь функцией *!!wiki {} (слово, то что ищите).*
        Можете удалить определенное количество сообщений; воспользуйтесь функцией *!!clears {} (кол-во сообщений для очистки)*.
        Можете задать таймер на определенное кол-во секунд; воспользуйтесь функцией *!!timer {}-{}* (колво минут-колво секунд).
        Можете узнать точную дату и время; воспользуйтесь функцией *!!date.*
        Можете подкинуть монетку; воспользуйтесь функцией *!!throw_coin*.
        Можете подкинуть кубики; воспользуйтесь функцией *!!throw_cubes {}* (кол-во кубиков).
        Можете решить легкое квадратное уравнение; воспользуйтесь функцией *!!solve_equation {} {} {}* 
(a b c из ax^2+bx+c=0)\n
Приятной работы со мной :sweat_smile:
Для тех кто хочет немножно аниме:blush:; воспользуйтесь *!!anime*""")

    # команда для получения мотивации
    @commands.command(name='random_advice')
    async def advice(self, ctx):
        responce = requests.get("https://api.adviceslip.com/advice").json()
        await ctx.send(
            f'English: {responce["slip"]["advice"]}\nРусский: {translate(responce["slip"]["advice"])}')
        if random.choice([1, 2]) == 1:
            response = requests.get("https://api.thecatapi.com/v1/images/search")
            answer = response.json()
            await ctx.send(f"Надеюсь фото кошечки поднимет тебе настроение:blush:")
            await ctx.send(answer[0]['url'])
        else:
            response = requests.get("https://dog.ceo/api/breeds/image/random")
            answer = response.json()
            await ctx.send(f"Надеюсь фото собачки поднимет тебе настроение:blush:")
            await ctx.send(answer['message'])

    # команда для получения информации из википедии
    """@commands.command(name='wiki')
    async def wiki(self, ctx, *infs):
        try:
            await ctx.send(f"Все что удалость найти:\n"
                           f"English: {str(wikipedia.page(' '.join([x for x in infs])).content[:250])}")
            # await ctx.send(
            #     f"Русский: {translate('en|ru', str(wikipedia.page(' '.join([x for x in infs])).content[:250]))}")
        except Exception:
            await ctx.send(f"Ошибка :space_invader:\n"
                           f"Вините во всем википедию")"""

    # функция для очистки сообщений
    @commands.command(name='clears')
    async def clears(self, ctx, amount=None):
        try:
            kolvo = int(amount)
            if kolvo > 11:
                await ctx.channel.send('Не пытайтесь удалить слишком много, вы можете навредить каналу.')
            else:
                await ctx.channel.purge(limit=kolvo)
                # await ctx.channel.send(':space_invader: Сообщения успешно удалены')
        except:
            await ctx.send(f"Ошибка :space_invader:\n"
                           f"Читайте *!!help_bot*")

    # функция для отправки рандомной аниме гифки (из имеющихся)
    @commands.command(name='anime')
    async def anime(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send(
            random.choice(["https://cdn.humoraf.ru/wp-content/uploads/2018/08/anime-gif-2.gif",
                           "https://media1.tenor.com/images/a477f2aa29494841f121d73a4bc30d55/tenor.gif?itemid=16945362",
                           "https://media1.tenor.com/images/730b8cb9f7c2bbece1eb9f093f5205ef/tenor.gif?itemid=5928196",
                           "https://media1.tenor.com/images/2ef78ab2f3e2acbf077388e26d3bc2da/tenor.gif?itemid=14815980",
                           "https://media1.tenor.com/images/09628191dbe81dcecc831e95a1f3e3d8/tenor.gif?itemid=7458570",
                           "https://media1.tenor.com/images/a44f316008d24797dc856c1dfd3a358d/tenor.gif?itemid=18100923",
                           "https://media1.tenor.com/images/933f8a346605b97c7e36b5cb0ae1924b/tenor.gif?itemid=17215102",
                           "https://media1.tenor.com/images/dd6393211b2201c997b3748dfcd9a659/tenor.gif?itemid=17837808",
                           "https://media1.tenor.com/images/2e77832cba70c65df33a229118af1c8e/tenor.gif?itemid=20701760",
                           "https://media1.tenor.com/images/f82fdfe817cfb8dacb5bd5c7dadb632d/tenor.gif?itemid=8718221",
                           "https://media1.tenor.com/images/26833e994e88a08d8cb702a7253327ac/tenor.gif?itemid=19924894",
                           "https://media1.tenor.com/images/3e674bb3a6e33e2f13c7d0a415af8674/tenor.gif?itemid=15235491",
                           "https://media.tenor.com/images/9e7f5606be05a52088c3806654cecf1b/tenor.gif",
                           "https://media.tenor.com/images/a669374af161a38cf2c7629480b86d02/tenor.gif",
                           "https://media.tenor.com/images/f7b2d47b80833b3fb972c7853b8adb22/tenor.gif",
                           "https://media.tenor.com/images/62eb1afcbb87252ddea4ae9574d731b5/tenor.gif"]))

    # Выводит пользователю рандомную гифку
    @commands.command(name="gif_r")
    async def random_gif(self, ctx):
        try:
            params = {'api_key': GIPHY_API_KEY,
                      'rating': 'r'}
            response = requests.request("GET", GIPHY_URL, params=params).json()
            gif_url = response["data"]["url"]
            await ctx.channel.purge(limit=1)
            await ctx.send(gif_url)
        except Exception:
            await ctx.send(f"Ошибка :space_invader:")

    # Ищет пользователю гифку по фразе и выводит ее
    @commands.command(name="gif_s")
    async def search_gif(self, ctx, *text):
        try:
            text = " ".join(text)
            params = {'api_key': GIPHY_API_KEY,
                      'tag': text,
                      'rating': 'r'}
            response = requests.request("GET", GIPHY_URL, params=params).json()
            gif_url = response["data"]["url"]
            await ctx.channel.purge(limit=1)
            await ctx.send(gif_url)
        except Exception:
            await ctx.send(f"Ошибка :space_invader:")

    @commands.command(name="ass")
    async def aaa(self, ctx):
        await ctx.channel.purge(limit=1)
        await ctx.send('Бот спать')
        await ctx.send('Миша сказал, что я сломался', tts='true')


# класс бота для работы с погодой
"""class WeatherBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # вспомогательная функция для получения информации о погоде о месте
    def get_weather_info(self, place, days=1):
        params = {"lat": get_coords(place).split(" ")[1],
                  "lon": get_coords(place).split(" ")[0],
                  "lang": "ru_RU",
                  "limit": days}
        headers = {"X-Yandex-API-Key": WEATHER_API_KEY}
        response = requests.get(WEATHER_URL, headers=headers, params=params).json()
        return response

    # команда для получения помощи для работы с погодой
    @commands.command(name='help_weather')
    async def help_weather(self, ctx):
        message = 'Вы можете воспользоваться двумя функциями: для информациями о погоде в выбранном городе ' \
                  'на текущее время *!!weather {}* (город) или для информации о погоде в выбранном городе' \
                  'на период до 7 дней *!!forecast {} {}* (город кол-во_дней).'
        await ctx.send(message)

    # команда для получения информации о погоде в выбранном городе на текущее время
    @commands.command(name="weather")
    async def current(self, ctx, place):
        try:
            response = self.get_weather_info(place)['fact']
            temperature = response['temp']
            pressure = response['pressure_mm']
            humidity = response['humidity']
            condition = response['condition']
            wind_dir = response['wind_dir']
            wind_seed = response['wind_speed']
            await ctx.send(
                f"Current weather in '{place}' today {datetime.now().date()} at time {datetime.now().hour}:"
                f"{datetime.now().minute}:\n"
                f"Temperature: {temperature}°,\n"
                f"Pressure: {pressure} mm,\n"
                f"Humidity: {humidity}%,\n"
                f"Condition: {condition},\n"
                f"Wind: {wind_dir}, {wind_seed} m/s.")
        except Exception:
            await ctx.send(f"Ошибка :space_invader:\n"
                           f"Читайте *!!help_weather*")

    # команда для получения информации о погоде в выбранном городе на период до 7 дней
    @commands.command(name="forecast")
    async def forecast(self, ctx, place, *days):
        try:
            days = int(days[0])
            if (len(str(days)) != 1) or (days < 1 or days > 7):
                raise ValueError
            answer = []
            response = self.get_weather_info(place, days=days)['forecasts']
            for forecast in response:
                date = forecast['date']
                day = forecast['parts']['day']
                temperature = day['temp_avg']
                pressure = day['pressure_mm']
                humidity = day['humidity']
                condition = day['condition']
                wind_dir = day['wind_dir']
                wind_seed = day['wind_speed']
                answer.append(f"Weather forecast in '{place}' for {date}:\n"
                              f"Temperature: {temperature}°,\n"
                              f"Pressure: {pressure} mm,\n"
                              f"Humidity: {humidity}%,\n"
                              f"Condition: {condition},\n"
                              f"Wind: {wind_dir}, {wind_seed} m/s.")
            await ctx.send("\n\n".join(answer))
        except Exception:
            await ctx.send(f"Ошибка :space_invader:\n"
                           f"Читайте *!!help_weather*")"""


# класс бота для работы с переводчиком
class TranslateBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # команда для получения помощи для работы с переводчиком
    @commands.command(name='help_translate')
    async def help_translate(self, ctx):
        message = 'Вы можете воспользоваться функцией для перевода фразы на русский язык\n с любого языка' \
                  '(будет определен автоматически) \n*!!translate {}* (текст).'
        await ctx.send(message)

    # команда для перевода перевода фразы
    @commands.command(name='translate')
    async def trans(self, ctx, *txt):
        await ctx.send(translate(" ".join(txt)))


# класс бота для работы с датой и временем
class DateBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # команда для запуска таймера
    @commands.command(name='timer')
    async def timer(self, ctx, ti):
        flag = False
        # Что-то сломали с pymorphy2
        """w1 = pymorphy2.MorphAnalyzer().parse('минута')[0]
        w2 = pymorphy2.MorphAnalyzer().parse('секунда')[0]
        w1.make_agree_with_number(minute).word"""
        try:
            minute = int(ti.split('-')[0])
            second = int(ti.split('-')[1])
            if second >= 60:
                a = second // 60
                minute += a
                second -= a * 60
            flag = True
            await ctx.send(
                f'Таймер сработает через {minute} минут и {second} секунд')
        except Exception:
            await ctx.send("Ошибка :space_invader:\n"
                           "Читайте *!!help_bot*")
        if flag:
            tim = minute * 60 + second
            await asyncio.sleep(tim)
            await ctx.send(
                f'Закончился таймер на {minute} минут и {second} секунд')

    # команда для получения точного времени
    @commands.command(name='date')
    async def dates(self, ctx):
        now = datetime.now()
        data = now.strftime("%B the %dth, %Y")
        time = now.strftime("%H:%M:%S on %A")
        await ctx.send(f'Дата: {data}\n'
                       f'Время: {time}')


# класс бота для работы с подсчетами
class MathBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # команда для броска монетки
    @commands.command(name='throw_coin')
    async def coins(self, ctx):
        dd = {
            1: 'орёл', 2: "решка", 3: "ребро"
        }
        dd1 = {
            1: 'Выпал', 2: "Выпала", 3: "Выпало"
        }
        data = random.choice([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3])
        await ctx.send(f'{dd1[data]} {dd[data]}')

    # команда для броска кубиков
    @commands.command(name='throw_cubes')
    async def cubes(self, ctx, cube):
        try:
            if int(cube) < 0:
                raise Exception
            if int(cube) >= 5:
                raise ValueError
            """w1 = pymorphy2.MorphAnalyzer().parse('очко')[0]
            w1.make_agree_with_number(dd[j]).word"""
            dd = [random.choice([1, 2, 3, 4, 5, 6]) for i in range(int(cube))]
            [await ctx.send(f"Из {str(j + 1)} кубика выпало *{str(dd[j])}* очков") for j in range(int(cube))]
        except ValueError:
            await ctx.send("Не пытайтесь получить слишком много, вы нагружаете бота слишком сильно.")
        except Exception:
            await ctx.send("Ошибка :space_invader:\n"
                           "Читайте *!!help_bot*")

    # команда для решения квадратных уравнений
    @commands.command(name='solve_equation')
    async def solve_eq(self, ctx, *abc):
        try:
            a, b, c = [int(x) for x in abc]
            d = eval("(b * b - 4 * a * c) ** 0.5")
            if d < 0:
                await ctx.send("В этом уравнение нет корней.")
            else:
                x1 = eval("(-b + d) / (2 * a)")
                x2 = eval("(-b - d) / (2 * a)")
                await ctx.send(
                    "Приносим извинения за то, что корни могут вычесляться огромными десятичными "
                    "дробями (мы стараемся сделать это лучше)\n"
                    f"X1: {x1}\n"
                    f"X2: {x2}")
        except Exception:
            await ctx.send("Ошибка :space_invader:\n"
                           "Читайте *!!help_bot*")


# класс бота для работы с геокодаром
class GeoBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # команда для получения помощи для работы с геокодаром
    @commands.command(name='help_geo')
    async def help_geo(self, ctx):
        message = 'Вы можете воспользоваться двумя функциями: для получения информации об адресе *!!geoinfo {}* (Адресс) или ' \
                  'для получения спутникого изображения *!!geofoto {}* (Адресс).'
        await ctx.send(message)

    # функция для получения информации об адресе
    @commands.command(name='geoinfo')
    async def geoinfo(self, ctx, *address):
        try:
            if address == ():
                raise Exception
            address = ' '.join(address)
            coords = get_coords(address)
            metro = Metro(coords)
            districts = district(coords)
            if coords is None and metro == 'Ноне (Ноне)' and districts == 'Ноне':
                raise Exception
            if metro == 'None':
                metro = "Метро нет, это глушь"
            if districts == 'None':
                districts = 'Район не удалось определить'
            if coords == 'None':
                coords = 'Координаты не удалось определить'
            else:
                coords = f'{coords.split(" ")[1]} {coords.split(" ")[0]}'
            await ctx.send(f'Информация по адресу *{address}*:\n'
                           f'Координаты: *{coords}*\n'
                           f'Метро: *{metro}*\n'
                           f'Район: *{districts}*\n')
        except Exception:
            await ctx.send("Ошибка :space_invader:\n"
                           "Читайте *!!help_geo*")

    # функция для получения спутникого изображения
    @commands.command(name='geofoto')
    async def geofoto(self, ctx, *address):
        try:
            if address == ():
                raise Exception
            address = ' '.join(address)
            coords = get_coords(address)
            if coords == 'None':
                raise Exception
            else:
                coords = ','.join(coords.split(' '))
            if len(address.split(' ')) > 1:
                map_request = f"https://static-maps.yandex.ru/1.x/?ll={coords}&l=sat,skl"
            else:
                map_request = f"https://static-maps.yandex.ru/1.x/?ll={coords}&z=8&l=sat,skl"
            await ctx.send(f'Спутниковое фото по адресу *{address}*\n{map_request}')
        except Exception:
            await ctx.send("Ошибка :space_invader:\n"
                           "Читайте *!!help_geo*")


# класс бота для ИГРЫ
class PlayBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.weapon = [1, 2, 3, 4]
        self.armor = [5, 6, 7, 8]
        self.artifacts = [9, 10, 11]

    # команда для получения помощи при игре
    @commands.command(name='help_play')
    async def help_play(self, ctx):
        await ctx.send("""Это небольшая рейд игра на боссов.
    Первым делом делом вам надо зайти в игру; используйте для этого *!!user*.
    Далее вы можете заработать 1 монету, для этого вам стоит подожать 3 секунды; используйте *!!earn_1*.
    Вы можете получить деньги за долгое отсутствие; используйте *!!check_earn*.
    Вы можете купить предметы в магазине; используйте *!!shop*, чтобы получить информацию 
и далее используйте *!!shop {} (номер предмета в магазине)*. Одновременно вы можете использовать только по 
одному типу из каждой категории.
    Вы можете посмотреть свою статистику; используйте для этого *!!stats*.
    Вы можете сменить свое оружие на одно из своих; используйте *!!weapon*, чтобы узнать какие
какие у вас есть и далее используйте *!!weapon {} (номер одного из своих оружий)*, чтобы сменить.
    Вы можете сменить свою броню на одну из своих; используйте *!!armor*, чтобы узнать какие
какие у вас есть и далее используйте *!!armor {} (номер одной из своей брони)*, чтобы сменить.
    Вы можете сменить свой артефакт на один из своих; используйте *!!artifacts*, чтобы узнать какие
какие у вас есть и далее используйте *!!artifacts {} (номер одного из своих артифактов)*, чтобы сменить.
    Вы можете совершить рейд на босса, чтобы поднять репутацию и заработать денег; используйте *!!boss*, чтобы узнать
информацию о боссах и далее используйте *!!boss {} (номер одного из боссов)*
    Вы можете удалять статистику; используйте *!!clear_st*""")

    # функция для входа в игру
    @commands.command(name="user")
    async def use(self, ctx):
        try:
            name = ctx.author.name
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            result = cur.execute(f"""SELECT * FROM Users
    WHERE name = '{name}'""").fetchall()
            if not result:
                cur.execute(
                    f"""INSERT INTO Users (name, last_activity, balance, rating, boss_clear, items, weapon, armor, artifacts) 
                    VALUES ('{name}', {datetime.now().hour * 3600 + datetime.now().minute * 60 + datetime.now().second},
                0, 0, '', '', 0, 0, 0)""")
                await ctx.send(f"Игрок {name} был авторизирован")
            else:
                await ctx.send(f"С возвращением, {name}!")
            con.commit()
            con.close()
        except Exception:
            await ctx.send("Ошибка :space_invader:\n"
                           "Читайте *!!help_play*")

    # функция для заработка 1 монетки
    @commands.command(name='earn_1')
    async def earn_1(self, ctx):
        await asyncio.sleep(3)
        try:
            names = ctx.author.name
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            result = cur.execute(f"""SELECT name FROM Users""").fetchall()
            if names in ' '.join([x[0] for x in result]):
                cur.execute(f"""UPDATE Users SET balance = balance + 1 WHERE name = '{names}'""")
                await ctx.send(f'Игрок *{names}* заработал *1 монетку*')
            else:
                await ctx.send(f"Нет игрока *{names}*")
            con.commit()
            con.close()
        except Exception:
            await ctx.send("Ошибка :space_invader:\n"
                           "У вас задержка, не фармите монеты слишком быстро:clown:.")

    # функция для заработка монеток при долгом отсутствии
    @commands.command(name='check_earn')
    async def check_earn(self, ctx):
        try:
            names = ctx.author.name
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            result = cur.execute(f"""SELECT name FROM Users""").fetchall()
            if names in ' '.join([x[0] for x in result]):
                result = cur.execute(f"""SELECT last_activity FROM Users Where name = '{names}'""").fetchone()[0]
                now = datetime.now().hour * 3600 + datetime.now().minute * 60 + datetime.now().second
                earn = abs(result - now) // 600
                cur.execute(
                    f"""UPDATE Users SET balance = balance + {earn}, last_activity = {now} WHERE name = '{names}'""")
                await ctx.send(f'Игрок *{names}* заработал *монет: {earn}*')
            else:
                await ctx.send(f"Нет игрока *{names}*")
            con.commit()
            con.close()
        except Exception:
            await ctx.send("Ошибка :space_invader:\n"
                           "Читайте *!!help_play*")

    # функция для покупки предметов
    @commands.command(name='shop')
    async def shop(self, ctx, ids=None):
        if ids is None:
            await ctx.send(
                """Вы можете купить вещи трех категорий: оружие, броню и артефакты.
    Для покупки напишите *!!shop {} (номер предмета в магазине)*. Номера вы можете посмотреть ниже:
Оружие:
|Номер---Цена----Название----------АТК---HP----DEF|
|1----------10-------Кинжал-------------100----0------15   |
|2----------15-------Длинный меч------150----0------30  |
|3----------20-------Меч Паладина----150----0------50  |
|4----------50-------Магический меч--250---0------15   |
Броня:
|Номер---Цена----Название------------------АТК---HP----DEF|
|5----------5--------Лохмотья бандита-------0-------25-----50  |
|6----------10-------Кольчуга рыцаря---------0-------50----75   |
|7----------75-------Божественная броня-----0------200---200|
|8----------15-------Магическая броня--------0------75-----75  |
Артефакты:
|Номер---Цена----Название--------------------АТК---HP----DEF|
|9----------40-------Кольцо жизни--------------20-----100---0    |
|10---------40-------Кольцо атаки---------------100----20----0    |
|11----------100-----Божественная благодать--150----150---0    |""")
        if ids is not None:
            try:
                names = ctx.author.name
                ids = int(ids)
                if ids > 11 or ids < 1:
                    raise ValueError
                con = sqlite3.connect(db_name)
                cur = con.cursor()
                result = cur.execute(f"""SELECT name FROM Users""").fetchall()
                if names in ' '.join([x[0] for x in result]):
                    balance = int(cur.execute(f"""SELECT balance FROM Users WHERE name ='{names}'""").fetchone()[0])
                    result = int(cur.execute(f"""SELECT cost FROM Shop WHERE id_items = {ids}""").fetchone()[0])
                    result_1 = cur.execute(f"""SELECT name, ATK, HP, DEF FROM Items WHERE id = {ids}""").fetchone()
                    result_1 = f'{result_1[0]}-{result_1[1]}-{result_1[2]}-{result_1[3]}'
                    haves = cur.execute(f"""SELECT items FROM Users WHERE name ='{names}'""").fetchone()[0].split(
                        ',')
                    have = sorted([int(x) for x in list(filter(lambda x: x, haves))], key=lambda x: x)
                    if ids in have:
                        await ctx.send(f'Игрок *{names}* уже имеет *{result_1}*.')
                    else:
                        if balance >= result:
                            have.append(ids)
                            if len(have) == 1:
                                have.append('')
                            else:
                                have = sorted(have, key=lambda x: x)
                            otv = ','.join([str(x) for x in have])
                            await ctx.send(f'Игрок *{names}* купил *{result_1}* за {result} монет.')
                            cur.execute(f"""UPDATE Users SET balance = balance - {result} WHERE name = '{names}'""")
                            cur.execute(f"""UPDATE Users SET items = '{otv}' WHERE name = '{names}'""")
                        else:
                            await ctx.send(f'Игрок *{names}* не смог купить *{result_1}*; не хватает монет.')
                else:
                    await ctx.send(f"Нет игрока *{names}*")
                con.commit()
                con.close()
            except ValueError:
                await ctx.send(f"Нет предмета под номером *{str(ids)}*\n"
                               "Читайте *!!shop*")
            except Exception:
                await ctx.send("Ошибка :space_invader:\n"
                               "Читайте *!!shop*")

    # функция для отображения статистики
    @commands.command(name='stats')
    async def statistic(self, ctx):
        try:
            names = ctx.author.name
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            result = cur.execute(f"""SELECT name FROM Users""").fetchall()
            if names in ' '.join([x[0] for x in result]):
                result = cur.execute(
                    f"""SELECT balance, rating, boss_clear, weapon, armor, artifacts FROM Users WHERE name = 
        '{names}'""").fetchone()
                result_1 = cur.execute(
                    f"""SELECT name, ATK, HP, DEF FROM Items WHERE id = {result[3]}""").fetchone()
                result_2 = cur.execute(
                    f"""SELECT name, ATK, HP, DEF FROM Items WHERE id = {result[4]}""").fetchone()
                result_3 = cur.execute(
                    f"""SELECT name, ATK, HP, DEF FROM Items WHERE id = {result[5]}""").fetchone()
                atk = result_1[1] + result_2[1] + result_3[1]
                hp = result_1[2] + result_2[2] + result_3[2]
                defend = result_1[3] + result_2[3] + result_3[3]
                result_1 = f'{result_1[0]}'
                result_2 = f'{result_2[0]}'
                result_3 = f'{result_3[0]}'
                bosses = result[2].split(',')
                boss = sorted([int(x) for x in list(filter(lambda x: x, bosses))], key=lambda x: x)
                if boss:
                    otv = []
                    for i in boss:
                        res = cur.execute(
                            f"""SELECT name, rating FROM Bosses WHERE id = {i}""").fetchone()
                        res = f'{res[0]}-{res[1]}'
                        otv.append(res)
                    otv = '; '.join(otv)

                else:
                    otv = 'Нет побежденных боссов'
                await ctx.send(f'Статистика игрока *{names}*:\n'
                               f'Рейтинг: {result[1]}.\n'
                               f'Баланс: {result[0]}.\n'
                               f'Побежденные боссы: {otv}.\n'
                               f'Оружие: {result_1}.\n'
                               f'Броня: {result_2}.\n'
                               f'Артифакт: {result_3}.\n'
                               f'ATK-HP-DEF: {atk}-{hp}-{defend}')
                haves = cur.execute(f"""SELECT boss_clear FROM Users WHERE name ='{names}'""").fetchone()[0].split(
                    ',')
                have = sorted([int(x) for x in list(filter(lambda x: x, haves))], key=lambda x: x)
                if have == [1, 2, 3, 4, 5, 6, 7, 8]:
                    await ctx.send(f"Игрок *{names}* прошел игру!!!")
            else:
                await ctx.send(f"Нет игрока *{names}*")
            con.commit()
            con.close()
        except Exception:
            await ctx.send("Ошибка :space_invader:\n"
                           "Читайте *!!help_play*")

    # функция для смены оружия
    @commands.command(name='weapon')
    async def weapon(self, ctx, ids=None):
        try:
            names = ctx.author.name
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            result = cur.execute(f"""SELECT name FROM Users""").fetchall()
            if names in ' '.join([x[0] for x in result]):
                haves = cur.execute(f"""SELECT items FROM Users WHERE name ='{names}'""").fetchone()[0].split(',')
                have = sorted([int(x) for x in list(filter(lambda x: x and int(x) in self.weapon, haves))],
                              key=lambda x: x)
                if ids is None:
                    await ctx.send("""Оружие:
|Номер-----Название----------АТК---HP----DEF|
|1------------Кинжал-------------100----0------15  |
|2------------Длинный меч------150----0------30|
|3------------Меч Паладина----150----0------50  |
|4------------Магический меч--250---0------15  |""")
                    await ctx.send(
                        f"У вас есть:\n{', '.join([cur.execute(f'SELECT name FROM Items WHERE id = {x}').fetchone()[0] for x in have])}")
                    await ctx.send(
                        "Воспользуйтесь функциуй *!!weapon {} (номер одного из своих оружий)*, чтобы сменить оружие.")
                if ids is not None:
                    ids = int(ids)
                    if ids > 11 or ids < 1:
                        raise ValueError
                    if ids not in self.weapon:
                        raise NameError
                    res = cur.execute(f'SELECT name FROM Items WHERE id = {ids}').fetchone()[0]
                    if ids in have:
                        cur.execute(f"""UPDATE Users SET weapon = {ids} WHERE name = '{names}'""")
                        await ctx.send(f'Оружие игрока *{names}* изменено на *{res}*')
                    else:
                        await ctx.send(f'Игрок *{names}* не имеет оружие: *{res}*')
            else:
                await ctx.send(f"Нет игрока *{names}*")
            con.commit()
            con.close()
        except NameError:
            await ctx.send(f"Предмет под номером *{str(ids)}* не является оружием")
        except ValueError:
            await ctx.send(f"Нет предмета под номером *{str(ids)}*\n"
                           "Читайте *!!weapon*")
        except Exception:
            await ctx.send("Ошибка :space_invader:\n"
                           "Читайте *!!help_play*")

    # функция для смены брони
    @commands.command(name='armor')
    async def armor(self, ctx, ids=None):
        try:
            names = ctx.author.name
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            result = cur.execute(f"""SELECT name FROM Users""").fetchall()
            if names in ' '.join([x[0] for x in result]):
                haves = cur.execute(f"""SELECT items FROM Users WHERE name ='{names}'""").fetchone()[0].split(',')
                have = sorted([int(x) for x in list(filter(lambda x: x and int(x) in self.armor, haves))],
                              key=lambda x: x)
                if ids is None:
                    await ctx.send("""Броня:
|Номер-----Название-----------------АТК---HP----DEF|
|5------------Лохмотья бандита------0-------25----50  |
|6------------Кольчуга рыцаря--------0-------50----75  |
|7------------Божественная броня----0------200---200|
|8------------Магическая броня-------0------75----75   |""")
                    await ctx.send(
                        f"У вас есть:\n{', '.join([cur.execute(f'SELECT name FROM Items WHERE id = {x}').fetchone()[0] for x in have])}")
                    await ctx.send(
                        "Воспользуйтесь функциуй *!!armor {} (номер одной из своей брони)*, чтобы сменить броню.")
                if ids is not None:
                    ids = int(ids)
                    if ids > 11 or ids < 1:
                        raise ValueError
                    if ids not in self.armor:
                        raise NameError
                    res = cur.execute(f'SELECT name FROM Items WHERE id = {ids}').fetchone()[0]
                    if ids in have:
                        cur.execute(f"""UPDATE Users SET armor = {ids} WHERE name = '{names}'""")
                        await ctx.send(f'Броня игрока *{names}* изменена на *{res}*')
                    else:
                        await ctx.send(f'Игрок *{names}* не имеет броню: *{res}*')
            else:
                await ctx.send(f"Нет игрока *{names}*")
            con.commit()
            con.close()
        except NameError:
            await ctx.send(f"Предмет под номером *{str(ids)}* не является броней")
        except ValueError:
            await ctx.send(f"Нет предмета под номером *{str(ids)}*\n"
                           "Читайте *!!armor*")
        except Exception:
            await ctx.send("Ошибка :space_invader:\n"
                           "Читайте *!!help_play*")

    # функция для смены артефактов
    @commands.command(name='artifacts')
    async def artifacts(self, ctx, ids=None):
        try:
            names = ctx.author.name
            con = sqlite3.connect(db_name)
            cur = con.cursor()
            result = cur.execute(f"""SELECT name FROM Users""").fetchall()
            if names in ' '.join([x[0] for x in result]):
                haves = cur.execute(f"""SELECT items FROM Users WHERE name ='{names}'""").fetchone()[0].split(',')
                have = sorted([int(x) for x in list(filter(lambda x: x and int(x) in self.artifacts, haves))],
                              key=lambda x: x)
                if ids is None:
                    await ctx.send("""Артефакты:
|Номер-----Название---------------------АТК-----HP----DEF|
|9------------Кольцо жизни---------------20-------100---0     |
|10-----------Кольцо атаки----------------100------20----0     |
|11------------Божественная благодать--150------150---0     |""")
                    await ctx.send(
                        f"У вас есть:\n{', '.join([cur.execute(f'SELECT name FROM Items WHERE id = {x}').fetchone()[0] for x in have])}")
                    await ctx.send(
                        "Воспользуйтесь функциуй *!!artifacts {} (номер одного из своих артефактов)*, чтобы сменить артефакт.")
                if ids is not None:
                    ids = int(ids)
                    if ids > 11 or ids < 1:
                        raise ValueError
                    if ids not in self.artifacts:
                        raise NameError
                    res = cur.execute(f'SELECT name FROM Items WHERE id = {ids}').fetchone()[0]
                    if ids in have:
                        cur.execute(f"""UPDATE Users SET artifacts = {ids} WHERE name = '{names}'""")
                        await ctx.send(f'Артефакт игрока *{names}* изменен на *{res}*')
                    else:
                        await ctx.send(f'Игрок *{names}* не имеет артефакт: *{res}*')
            else:
                await ctx.send(f"Нет игрока *{names}*")
            con.commit()
            con.close()
        except NameError:
            await ctx.send(f"Предмет под номером *{str(ids)}* не является артефактом")
        except ValueError:
            await ctx.send(f"Нет предмета под номером *{str(ids)}*\n"
                           "Читайте *!!artifacts*")
        except Exception:
            await ctx.send("Ошибка :space_invader:\n"
                           "Читайте *!!help_play*")

    # функция для смены артефактов
    @commands.command(name='boss')
    async def boss(self, ctx, ids=None):
        # try:
        names = ctx.author.name
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        result = cur.execute(f"""SELECT name FROM Users""").fetchall()
        if names in ' '.join([x[0] for x in result]):
            haves = cur.execute(f"""SELECT boss_clear FROM Users WHERE name ='{names}'""").fetchone()[0].split(
                ',')
            have = sorted([int(x) for x in list(filter(lambda x: x, haves))], key=lambda x: x)
            if ids is None:
                await ctx.send("""Боссы:
|Номер-----Название--------------Рейтинг-----Награда-----MIN_АТК-----MIN_HP----MIN_DEF|
|1------------Волк--------------------50------------3-------------50--------------10-----------20            |
|2------------Медведь---------------100----------5-------------100-------------25-----------30            |
|3------------Вор---------------------120-----------6-------------120-------------30-----------30           |
|4------------Грифон----------------200-----------15------------140------------50-----------75            |
|5------------Каменный голем-----250-----------20-----------150-------------75-----------80           |
|6------------Травянной монстр---300-----------50-----------200------------75-----------85           |
|7------------Дракон-----------------500----------100----------250-------------120----------90          |
|8------------Бог----------------------1500---------200---------400-------------300---------200        |""")
                await ctx.send(
                    f"Вы прошли:\n{', '.join([cur.execute(f'SELECT name FROM Bosses WHERE id = {x}').fetchone()[0] for x in have])}")
                await ctx.send(
                    "Воспользуйтесь функциуй *!!boss {} (номер одного из боссов)*, чтобы начать охоту.")
            if ids is not None:
                ids = int(ids)
                if ids > 8 or ids < 1:
                    raise ValueError
                res = cur.execute(
                    f'SELECT name, rating, balance, min_atk, min_hp, min_def FROM Bosses WHERE id = {ids}').fetchone()
                if ids in have:
                    # cur.execute(f"""UPDATE Users SET artifacts = {ids} WHERE name = '{names}'""")
                    await ctx.send(f'Игрока *{names}* уже прошел *{res[0]}*')
                else:
                    result = cur.execute(
                        f"""SELECT balance, rating, boss_clear, weapon, armor, artifacts FROM Users WHERE name = 
                            '{names}'""").fetchone()
                    result_1 = cur.execute(
                        f"""SELECT name, ATK, HP, DEF FROM Items WHERE id = {result[3]}""").fetchone()
                    result_2 = cur.execute(
                        f"""SELECT name, ATK, HP, DEF FROM Items WHERE id = {result[4]}""").fetchone()
                    result_3 = cur.execute(
                        f"""SELECT name, ATK, HP, DEF FROM Items WHERE id = {result[5]}""").fetchone()
                    my_atk = result_1[1] + result_2[1] + result_3[1]
                    my_hp = result_1[2] + result_2[2] + result_3[2]
                    my_defend = result_1[3] + result_2[3] + result_3[3]
                    atk, hp, defend = res[3], res[4], res[5]
                    balances = res[2]
                    ratings = res[1]
                    if my_atk < atk:
                        await ctx.send(f'Игроку *{names}* не хватает очков атаки: {atk - my_atk}')
                    elif my_hp < hp:
                        await ctx.send(f'Игроку *{names}* не хватает очков здоровья: {hp - my_hp}')
                    elif my_defend < defend:
                        await ctx.send(f'Игроку *{names}* не хватает очков защиты: {defend - my_defend}')
                    else:
                        have.append(ids)
                        if len(have) == 1:
                            have.append('')
                        else:
                            have = sorted(have, key=lambda x: x)
                        otv = ','.join([str(x) for x in have])
                        await ctx.send(
                            f'Игрок *{names}* получил *монет: {balances}*, *очков рейтинга: {ratings}*; за победу над боссом *{res[0]}*')
                        cur.execute(
                            f"""UPDATE Users SET balance = balance + {balances} WHERE name = '{names}'""")
                        cur.execute(f"""UPDATE Users SET rating = rating + {ratings} WHERE name = '{names}'""")
                        cur.execute(f"""UPDATE Users SET boss_clear = '{otv}' WHERE name = '{names}'""")
                        if have == [1, 2, 3, 4, 5, 6, 7, 8]:
                            await ctx.send(f"Игрок *{names}* прошел игру!!!")
        else:
            await ctx.send(f"Нет игрока *{names}*")
        con.commit()
        con.close()
        # except ValueError:
        #     await ctx.send(f"Нет босса под номером *{str(ids)}*\n"
        #                    "Читайте *!!boss*")
        # except Exception:
        #     await ctx.send("Ошибка :space_invader:\n"
        #                    "Читайте *!!help_play*")

    # функция для удаления статистики
    @commands.command(name='clear_st')
    async def clear_st(self, ctx, dat=None):
        if dat is None:
            await ctx.send(
                """С помощью этой функции вы можете стирать статистику:
Функция *!!clear_st items* - сменяет выбранное оружие, броню и артефакт на начальные (ничего).
Функция *!!clear_st inventory* - стирает все предметы (деньги не возвращаются).
Функция *!!clear_st boss* - стирает статистику боссов и рейтинга, который выпал за них.
Функция *!!clear_st balance* - обнуляет ваш баланс.
Функция *!!clear-st all* - стирает аккаунт.
Пожалуйста будьте аккуратны, функцию отменить нельзя""")
        if dat is not None:
            try:
                names = ctx.author.name
                con = sqlite3.connect(db_name)
                cur = con.cursor()
                result = cur.execute(f"""SELECT name FROM Users""").fetchall()
                if names in ' '.join([x[0] for x in result]):
                    if dat == 'all':
                        cur.execute(f"DELETE FROM Users WHERE  name ='{names}'")
                        await ctx.send(
                            f"Аккаунт игрока *{names}* был удален.\nИспользуйте *!!user*, чтобы создать новый аккаунт.")
                    elif dat == 'items':
                        cur.execute(f"UPDATE Users SET weapon = 0, armor = 0, artifacts = 0 WHERE name = '{names}'")
                        await ctx.send(
                            f"Игрок *{names}* сменил оружие, броню и артефакт на начальные.")
                    elif dat == 'inventory':
                        cur.execute(f"UPDATE Users SET items = '' WHERE name = '{names}'")
                        await ctx.send(
                            f"Игрок *{names}* удалил все свои предметы.")
                    elif dat == 'balance':
                        cur.execute(f"UPDATE Users SET balance = 0 WHERE name = '{names}'")
                        await ctx.send(
                            f"Игрок *{names}* обнулил свой баланс.")
                    elif dat == 'boss':
                        cur.execute(f"UPDATE Users SET boss_clear = '', rating = 0 WHERE name = '{names}'")
                        await ctx.send(
                            f"Игрок *{names}* удалил статистику побежденных боссов, тем самым обнулив рейтинг.")
                    else:
                        await ctx.send("Бот не может определить вашу команду:space_invader:\n"
                                       "Читайте *!!clear_st*")
                else:
                    await ctx.send(f"Нет игрока *{names}*")
                con.commit()
                con.close()
            except Exception:
                await ctx.send("Ошибка :space_invader:\n"
                               "Читайте *!!clear_st*")


# Запускает нашего бота
if __name__ == "__main__":
    bot = MyBot()
    bot.run(BOT_TOKEN)
