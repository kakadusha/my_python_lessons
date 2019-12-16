# Код бота взят отсда:
# https://github.com/eternnoir/pyTelegramBotAPI#getting-started
# как обойти роскомнадзор через socks 5^ https://toster.ru/q/524178
#

import telebot

bot = telebot.TeleBot("(двагуся)699(трижопы)2:AAF7zUPzN-NcmdgW5R0hzhItTCtD1RsvjYs")

from telebot import apihelper

# прокси
apihelper.proxy = {'https':'socks5://127.0.0.1:9100'}
                           
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()