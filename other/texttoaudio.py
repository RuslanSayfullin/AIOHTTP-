from gtts import gTTS
import os

text = "Hello!"
language = 'ru'

# Создаем обьект gTTS и сохраняем аудиофайл
tts = gTTS(text=text, lang = language)
tts.save("hello.mp3")

# Воспроизводим аудиофайл
os.system("mpg321 hello.mp3")
