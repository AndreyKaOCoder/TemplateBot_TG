import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

bot = Bot("") #YOUR TOKEN
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer(f"Hello World!")

async def main():
    await bot.delete_webhook(drop_pending_updates = True) #Skips messages sent when the bot is turned off
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())