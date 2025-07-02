import keyboard
import speech_recognition
import os
import random
from gtts import gTTS
from playsound import playsound

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.4
sr.non_speaking_duration = 0.3

flag = True

TEXT_ERROR = 'Damn... Не понял что ты сказал :/'
language = 'ru'

commands_dict = {
    'commands': {
        'greeting': ['привет', "здарова"],
        'create_task': ['добавь задачу', "создай задачу", "заметка"],
        'play_music': ["включи музыку", "дискотека"],
        'end_bot': ['конец', "закройся", "выключись", "пока"]
    },
    'author':{
        
    }
}


def listen_command():
    playsound('data/listen.mp3')
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language="ru-RU").lower()
        playsound('data/end.mp3')
        return query
    except speech_recognition.UnknownValueError:
        playsound('data/error.mp3')
        return TEXT_ERROR


def greeting():
    playsound('data/greeting.mp3')


def end_bot():
    global flag
    playsound('data/end_bot.mp3')
    flag = False


def create_task():
    playsound('data/task.mp3')
    query = listen_command()

    if query != TEXT_ERROR:
        with open('todo-list.txt', 'a') as file:
            file.write(f'{query}\n')
        text_val = f'Задача {query} добавлена в список дел'
        text_val.encode('utf8')
        obj = gTTS(text=text_val, lang=language, slow=False)
        obj.save('data/end_task.mp3')
        playsound('data/end_task.mp3')


def play_music():
    """Функция для проигрования аудиофайлов"""
    files = os.listdir('music')
    random_file = f'music/{random.choice(files)}'
    os.system('start ' + random_file)
    print(f'Музыка запущена {random_file.split("/")[-1]}')


def main():
    while flag:
        if keyboard.is_pressed(keyboard.KEY_UP):
            query = listen_command()
            h = 0
            if query != TEXT_ERROR:
                for k, v in commands_dict['commands'].items():
                    if query in v:
                        h = 1
                        globals()[k]()
                if h == 0:
                    playsound("data/none.mp3")


if __name__ == '__main__':
    main()
