import telebot

bot = telebot.TeleBot('7229031292:AAFNoSpyzVMAk5f6uMSbB1wkA3GZy5od0II')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler()
def z(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)