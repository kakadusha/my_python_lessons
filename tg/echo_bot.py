# Код бота взят отсда:
# https://github.com/eternnoir/pyTelegramBotAPI#getting-started
# как обойти роскомнадзор через socks 5^ https://toster.ru/q/524178
#

import telebot

bot = telebot.TeleBot("226993332:AAF7zUPzN-NcmdgW5R0hzhItTCtD1RsvjYs")
# 206719458:AAGVut78WMo8V_XieOqqAo6HSjWpn0k1nUY  -- heco bot tocken (@HBCoachBot)
# 228216676:AAF4DDbdh-MTciXHuWG-d3JeJOi1ZTI-_A0  -- heprot bot tocken (@HeProtBot) 
# 226993332:AAF7zUPzN-NcmdgW5R0hzhItTCtD1RsvjYs  -- AsBot  tocken(@AstrologRubot)

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