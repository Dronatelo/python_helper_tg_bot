from aiogram.types import ReplyKeyboardMarkup

valute_name = ['RUB','USD','EUR','UAH','KZT', 'CNY', 'AMD','↩MENU']
valutes = ReplyKeyboardMarkup(resize_keyboard=True)
valutes.add(*valute_name)
