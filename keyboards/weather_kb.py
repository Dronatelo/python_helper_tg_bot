from aiogram.types import ReplyKeyboardMarkup

cites = ['*','*','*','↩MENU']
city_name = ReplyKeyboardMarkup(resize_keyboard=True)
city_name.add(*cites)
