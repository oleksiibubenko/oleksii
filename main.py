
import telebot

import requests
from bs4 import BeautifulSoup as BS

bot = telebot.TeleBot('1389644568:AAGor0AV0KL8yB9oh8Dx2M66aD9wWYw-As0')

r = requests.get('https://ua.sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BC%D0%B0%D0%B9%D0%B4%D0%B0%D0%BD-303014685')
html = BS(r.content, 'html.parser')


for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    text = el.select('.wDescription .description')[0].text

@bot.message_handler(commands=['start', 'help'])
def main(message):
	bot.send_message(message.chat.id,  " Привіт, погода на сьогодні:\n" +
        t_min + ', ' + t_max + '\n' +text)

if __name__ == '__main__':
    bot.polling(none_stop=True)



