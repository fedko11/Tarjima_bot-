from aiogram.fsm.state import State,StatesGroup
from gtts import gTTS


class Translate(StatesGroup):
    lang = State()
    trans = State()
    audio = State()
 

def speech(mytext, lan):
    myobj = gTTS(text=mytext, lang=lan, slow=False)
    myobj.save('audio.mp3')