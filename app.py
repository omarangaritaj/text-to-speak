from gtts import gTTS
import os


txt = input('Inserte el texto a convertir a audio: ')
gtts = gTTS(text=txt, lang='es', tld='com.mx')

gtts.save('text.mp3')
os.system('text.mp3')
