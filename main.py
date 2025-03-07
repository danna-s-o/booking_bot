from aiogram import Bot, Dispatcher
from booking_bot.utils.config import TOKEN
import asyncio
import logging
from booking_bot.handlers.booking import router as booking_router
from booking_bot.handlers.payment import router as payment_router
from booking_bot.database.models import createRestaurantDatabase
from booking_bot.database.crud import is_tables_empty, add_tables_data

async def main():

    logging.basicConfig(level=logging.INFO)
    createRestaurantDatabase()

    if is_tables_empty():
        add_tables_data()
    else:
        logging.info("Таблица столиков уже содержит данные. Пропускаем заполнение.")

    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_routers(booking_router, payment_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())