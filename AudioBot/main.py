from gtts import gTTS
from playsound import playsound

text_val = "Даша сосочка"
language = 'ru'

obj = gTTS(text=text_val, lang=language, slow=False)

obj.save('data/new_sound.mp3')
playsound('data/new_sound.mp3')

