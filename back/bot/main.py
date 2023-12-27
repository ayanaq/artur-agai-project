from aiogram import Bot, Dispatcher, types

Token = ('6056293459:AAHDtkk-QTHrlN5v8P5pidlUVDjZLw2iR3Q')

bot = Bot(Token)
dp = Dispatcher(bot=bot)

async def echo(user, obj):
    await bot.send_message(chat_id=1154757842, text=f'{user} bought "{obj}"')