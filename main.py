from gtts import gTTS
from playsound import playsound

text_val = "у меня нет такой возможности"
text_val.encode('utf8')
language = 'ru'

obj = gTTS(text=text_val, lang=language, slow=False)

obj.save('AudioBot/data/none.mp3')
playsound('AudioBot/data/none.mp3')

