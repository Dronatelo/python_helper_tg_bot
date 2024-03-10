from datetime import date
from aiogram import types,Dispatcher
from aiogram.dispatcher.filters import Text

# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters.state import StatesGroup, State

# from keyboards.main_kb import main_menu,menu
from settings.money_info_code import get_money_usd,get_money_eur,get_money_kzt,get_money_uah,get_money_cny,get_money_amd,get_btc_info
#@dp.message_handler(Text(equals = '💰'))
async def get_info_money(message: types.Message):
    await message.answer(
    "💸 MONEY 📰"+"\n" \
    "USD: "+"$"+get_money_usd()+"\n" \
    "EURO: "+"€"+get_money_eur()+"\n" \
    "KZT: "+"₸"+get_money_kzt()+"\n" \
    "UAH: "+"₴"+get_money_uah()+"\n" \
    "CNY: "+"¥"+get_money_cny()+"\n" \
    "AMD: "+"֏"+get_money_amd()+"\n" \
    "💳 CRYPTO 💎"+"\n" \
    "BTC: "+get_btc_info())
    # "ETH: "+"¥"+get_eth_info())
    
def register_handlers_money_info(dp: Dispatcher):
    dp.register_message_handler(get_info_money, Text(equals="💰"),state=None)
