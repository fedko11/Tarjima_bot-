BOT_TOKEN = '6875811312:AAHBk2_Vu5rzhlPCD19ix2yYwCWVDNB20Hw'
from gtts import gTTS



def speech(mytext, lan):
    myobj = gTTS(text=mytext, lang=lan, slow=False)
    myobj.save('audio.mp3')