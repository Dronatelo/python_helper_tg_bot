from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

#ip_finder_bt = KeyboardButton("🌐")  <-- доделать функцию для корректной работы
money_info_bt = KeyboardButton("💰")
weather_info_bt = KeyboardButton("⛅")
conver_money_bt = KeyboardButton("💱")
#data_coder_bt = KeyboardButton("🔐") <-- cоздать функцию для шифровки файлов и отправки их на сервер

menu_bt = KeyboardButton("↩MENU")
start_bt = KeyboardButton("/start")

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu = ReplyKeyboardMarkup(resize_keyboard=True)
start_button = ReplyKeyboardMarkup(resize_keyboard=True)

main_menu.add(money_info_bt,weather_info_bt,conver_money_bt)
menu.add(menu_bt)
start_button.add(start_bt)