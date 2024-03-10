from aiogram import executor
from create_bot import dp
from handlers import start_connect,money_info,weather,convert_money

async def on_startup(_):
    print("Bot Online!")
    
start_connect.register_handlers_start_connect(dp)
money_info.register_handlers_money_info(dp)
weather.register_handlers_weather(dp)
convert_money.register_handlers_coder_valute(dp)

def main():
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    
main()