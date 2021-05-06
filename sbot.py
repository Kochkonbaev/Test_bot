import telebot

bot = telebot.TeleBot('1207780871:AAFU9CsenDDc1wrXCSqSR5FWo_4niOF-uUA')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, как тебя зовут?')


bot.polling()
