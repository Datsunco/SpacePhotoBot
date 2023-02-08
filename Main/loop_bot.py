from aiogram import executor
from Main.create_bot import dp


async def on_startup(self):
    print("В онлайне")


from Handlers import start_handler as start
start.register_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)