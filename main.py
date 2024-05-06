import asyncio
import logging
import sys
from os import getenv
from config import BOT_TOKEN 
from aiogram import Bot, Dispatcher, html ,F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message,CallbackQuery,FSInputFile
from button import menyu , voice
from aiogram.fsm.context import FSMContext
from states import Translate,speech
import os
from googletrans import Translator

bot = Bot(token=BOT_TOKEN)
t = Translator()

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
   await message.answer(f"Assalomu alaykum Tarjima tilini tanlang!" , reply_markup=menyu)
   await state.set_state(Translate.lang)





@dp.message(F.text,Translate.lang)
async def echo_handler(message: Message, state: FSMContext) -> None:
    translate_text = message.text
    await state.update_data(
        {'translate_text':translate_text}
    )
    await state.set_state(Translate.trans)
    await message.answer(f"Tarjima qilmoqchi bo'lgan textni kiriting")
    
    
    
    
@dp.message(F.text, Translate.trans)
async def translate(message: Message, state: FSMContext) -> None:
    text = message.text
    a = await state.get_data()
    tarjima = a.get('translate_text')
    if tarjima == '🇺🇿UZ -> 🇷🇺RU':
        xabar = t.translate(text, dest='ru').text
        await message.answer(f"Sizning so'zingiz ruschada\n  {xabar} deb tarjima qilinadi! " , reply_markup=voice)
        speech(text, 'ru')
    elif tarjima == '🇷🇺RU -> 🇺🇿UZ':
        xabar = t.translate(text, dest='uz').text
        await message.answer(f"Sizning so'zingiz o'zbekchada\n  {xabar} deb tarjima qilinadi! ",reply_markup=voice)
        speech(text, 'tr')
    elif tarjima == '🇺🇿UZ -> 🇺🇸EN':
        xabar = t.translate(text=xabar, dest='en').text
        await message.answer(f"Sizning so'zingiz Inglizchada\n  {xabar} deb tarjima qilinadi! ",reply_markup=voice) 
        speech(text, 'en')
    elif tarjima == '🇺🇸EN -> 🇺🇿UZ ':
        xabar = t.translate(text, dest='uz').text
        await message.answer(f"Sizning so'zingiz o'zbekchada\n  {xabar} deb tarjima qilinadi! ",reply_markup=voice) 
        speech(text, 'tr')
    await state.set_state(Translate.audio)    
     
@dp.callback_query(Translate.audio)
async def get_voice(call: CallbackQuery, state: FSMContext):
    audio = FSInputFile('audio.mp3')
    await bot.send_audio(call.message.chat.id, audio)
    os.remove('audio.mp3')
    await state.clear() 
        
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print("bot o`chdi")