from aiogram import Bot, Dispatcher, executor, types


bot = Bot('6636572525:AAF5L5YYgczRpg_cmACJq4GhmTbFv-Ltz3U')
dp = Dispatcher(bot)


@dp.message_handler(commands=['give'])
async def send_sticker(message: types.Message):
    await message.answer('Смотри какой Райн Гослинг❤️')
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEKfXplI_mqjCcrdNXIc3uNDcNoVhZTbAACPygAAtdLsEi8-quOfW05wDAE')


@dp.message_handler()
async def send_sticker(message: types.Message):
    if message.text == "❤️":
        await message.answer("🖤")


if __name__ == '__main__':
    executor.start_polling(dp)
