from aiogram import types,Dispatcher
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

import settings.money_info_code
from settings.conver_money_code import convert_currency
from keyboards.main_kb import main_menu
from keyboards.converter_kb import valutes

class valute_converter(StatesGroup):
    valute_one=State()
    value_valute=State()
    valute_two=State()

def sim_valute(str_valute):
    if str_valute == "RUB" or str_valute == "rub" :
        return "₽"
    elif str_valute == "USD" or str_valute == "usd" :
        return "$"
    elif str_valute == "EUR" or str_valute == "eur" :
        return "€"
    elif str_valute == "CNY" or str_valute == "cny" :
        return "¥"
    elif str_valute == "AMD" or str_valute == "amd" :
        return "֏"
    elif str_valute == "KZT" or str_valute == "kzt" :
        return "₸"
    elif str_valute == "UAH" or str_valute == "uah" :
        return "₴"

#@dp.message_handler(Text(equals='💱'))
async def valute_selecter(message: types.Message):
    await message.answer("Кодировка валют:"+"\n"+
                         "[₽] RUB - Рубль"+"\n"+
                         "[$] USD - Доллар"+"\n"+
                         "[€] EUR - Евро"+"\n"+
                         "[₴] UAH - Гривна"+"\n"+
                         "[₸] KZT - Тенге"+"\n"+
                         "[¥] CNY - Юань"+"\n"+
                         "[֏] AMD - Драм")

    await message.answer("Какую валюту хотите обменять?", reply_markup=valutes)
    await valute_converter.valute_one.set()

#@dp.message_handler(state="*",commands = "cancel")
#@dp.message_handler(Text(equals='cancel',ignore_case=True),state="*")
async def cancel_handler(message: types.Message,state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer("Вы возвращены в меню!",reply_markup=main_menu)

#@dp.message_handler(state=valute_converter.valute_one)
async def get_named_first_valute(message: types.Message, state: FSMContext):
    valute_one = message.text
    if valute_one == "↩MENU":
        await message.answer('Вы возвращены в меню❗', reply_markup=main_menu)
        await state.finish()
    else:
        async with state.proxy() as data:
                data['valute_one'] = valute_one
        await message.answer("Сколько "+valute_one+" хотите конвертировать?")
        await valute_converter.value_valute.set()

#@dp.message_handler(state=valute_converter.value_valute)
async def get_value_valute(message: types.Message, state: FSMContext):
    value_valute = message.text
    if value_valute == "↩MENU":
        await message.answer('Вы возвращены в меню❗', reply_markup=main_menu)
        await state.finish()
    else:
        async with state.proxy() as data:
                data['value_valute'] = value_valute 
        await message.answer("На какую валюту хотите обменять?")
        await valute_converter.valute_two.set()

#@dp.message_handler(state=valute_converter.valute_two)
async def get_named_twice_valute(message: types.Message, state: FSMContext):
    valute_two = message.text
    if valute_two == "↩MENU":
        await message.answer('Вы возвращены в меню❗', reply_markup=main_menu)
        await state.finish()
    else:
        async with state.proxy() as data:
            valute_one = data['valute_one']
            value_valute = data['value_valute']

        value_valute_int = int(value_valute)

        result = convert_currency(valute_one,valute_two,value_valute_int)
        res_simv = sim_valute(valute_two)

        await message.answer(f"{result}{res_simv}", reply_markup=main_menu)
        await state.finish()

def register_handlers_coder_valute(dp: Dispatcher):
    dp.register_message_handler(valute_selecter, Text(equals="💱"),state=None)
    dp.register_message_handler(cancel_handler,state="*",commands="cancel")
    dp.register_message_handler(cancel_handler,Text(equals='cancel',ignore_case=True),state="*")
    dp.register_message_handler(get_named_first_valute,state=valute_converter.valute_one)
    dp.register_message_handler(get_value_valute,state=valute_converter.value_valute)
    dp.register_message_handler(get_named_twice_valute,state=valute_converter.valute_two)
