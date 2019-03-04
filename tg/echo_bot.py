# Код бота взят отсда:
# https://github.com/eternnoir/pyTelegramBotAPI#getting-started
# как обойти роскомнадзор через socks 5^ https://toster.ru/q/524178
#

import telebot

bot = telebot.TeleBot("228216676:AAF4DDbdh-MTciXHuWG-d3JeJOi1ZTI-_A0")
# 206719458:AAGVut78WMo8V_XieOqqAo6HSjWpn0k1nUY  -- heco bot tocken (@HBCoachBot)
# 228216676:AAF4DDbdh-MTciXHuWG-d3JeJOi1ZTI-_A0  -- heprot bot tocken (@HeProtBot) 


from telebot import apihelper

# Витин прокси: socks5://10.8.5.20:9050
apihelper.proxy = {'https':'socks5://10.8.5.20:9050'}
                           
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()