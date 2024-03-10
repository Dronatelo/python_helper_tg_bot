from aiogram import types,Dispatcher
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from keyboards.main_kb import main_menu
from keyboards.weather_kb import city_name
from settings.weather_code import get_weather

class get_weather_info(StatesGroup):
    wather_info=State()

#@dp.message_handler(Text(equals = '⛅'))
async def get_name_city(message: types.Message):
    await message.answer("Введите название города", reply_markup=city_name)
    await get_weather_info.wather_info.set()

#@dp.message_handler(state="*",commands = "cancel")
#@dp.message_handler(Text(equals='cancel',ignore_case=True),state="*")
async def cancel_handler(message: types.Message,state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer("Вы возвращены в меню!",reply_markup=main_menu)

#@dp.message_handler(state=get_weather_info.wather_info)
async def get_info_weather(message: types.Message, state: FSMContext):
    city_name = message.text
    if city_name == "↩MENU":
        await message.answer('Вы возвращены в меню❗', reply_markup=main_menu)
        await state.finish()
    else:
        await message.answer(get_weather(city_name),reply_markup=main_menu)
        await state.finish()

def register_handlers_weather(dp: Dispatcher):
    dp.register_message_handler(get_name_city, Text(equals="⛅"),state=None)
    dp.register_message_handler(cancel_handler,state="*",commands="cancel")
    dp.register_message_handler(cancel_handler,Text(equals='cancel',ignore_case=True),state="*")
    dp.register_message_handler(get_info_weather,state=get_weather_info.wather_info)
