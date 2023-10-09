import telebot
import webbrowser

bot = telebot.TeleBot('6392178713:AAHWZiUsSw3qkDgag7QaP_UOxPok8jBQh_I')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.reply_to(message, 'Красивое фото!')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.youtube.com')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет!, {message.from_user.first_name} {message.from_user.username}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Help information', parse_mode='html')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.username}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)
