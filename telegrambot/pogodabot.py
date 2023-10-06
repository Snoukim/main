import telebot
import requests
import json

bot = telebot.TeleBot('6547270383:AAEJONA2xRJJbB2Vb12MyL1vNNyFFkuMe6c')
API = 'ea5084e78cf1efcdcd851828d9355994'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(res.text)
    temp = data["main"]["temp"]
    bot.reply_to(message, f'Сейчас погода: {temp}')

    image = 'sunny.jpg' if temp > 5.0 else 'sun.png'
    file = open('./' + image, 'rb')
    bot.send_photo(message.chat.id, file)


bot.polling(none_stop=True)
