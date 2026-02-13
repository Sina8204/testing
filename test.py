from send_receave_request import models
import telebot as tb
import os

TOKEN = os.getenv("bt")
Key = os.getenv("key")

content_creator = models(key=Key)
bot = tb.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_cmd(message):
    text = content_creator.send_requiest_to_model(
        "Write a beautiful welcome message",
        "Write a beautiful welcome message"
    )
    bot.send_message(message.chat.id, f"welcome dear\n{text}")

@bot.message_handler(commands=['username'])
def username_cmd(message):
    username = message.from_user.username or "unknown"
    bot.send_message(message.chat.id, f"welcome dear {username}")

@bot.message_handler(commands=['name'])
def name_cmd(message):
    bot.send_message(message.chat.id, f"welcome dear {message.from_user.first_name}")

bot.delete_webhook()
bot.polling(none_stop=True)
