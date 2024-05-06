from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
menyu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=' 🇺🇿UZ -> 🇷🇺RU ') , KeyboardButton(text=' 🇷🇺RU -> 🇺🇿UZ ')],
        [KeyboardButton(text=' 🇺🇸EN -> 🇺🇿UZ ') , KeyboardButton(text=' 🇺🇿UZ -> 🇺🇸EN ')],
    
    ],resize_keyboard=True
)

voice = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text="audio")]
    ],resize_keyboard = True
)