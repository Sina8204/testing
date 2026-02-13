import telebot as tb
bot = tb.TeleBot('8064045709:AAFd6qIg8UdrsyooR9o27E7n6hHPEeSvYO8')

@bot.message_handler(commands = ['start'])
def welcome(message):
  bot.send_message(message.chat.id , f'welcom dear')

@bot.message_handler(commands = ['username'])
def welcome(message):
  bot.send_message(message.chat.id , f'welcom dear {message.chat.username}')

@bot.message_handler(commands = ['name'])
def welcome(message):
  bot.send_message(message.chat.id , f'welcom dear {message.chat.first_name}')

bot.delete_webhook()
bot.polling()
