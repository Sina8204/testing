import telebot as tb
import os
from send_receave_request import models

TOKEN = os.getenv("bt")
KEY = os.getenv("key")

bot = tb.TeleBot(TOKEN)
content_creator = models(key=KEY)

# --- Handlers ---

@bot.message_handler(commands=['start'])
def start_cmd(message):
    try:
        text = content_creator.ask(
            "پاسخ را فقط فارسی، کوتاه و حداکثر دو جمله بنویس.",
            "یک پیام خوش‌آمدگویی زیبا بنویس."
        )
        bot.send_message(message.chat.id, text)
    except Exception as e:
        bot.send_message(message.chat.id, f"خطا در پردازش: {e}")

@bot.message_handler(commands=['username'])
def username_cmd(message):
    username = message.from_user.username or "کاربر عزیز"
    bot.send_message(message.chat.id, f"سلام {username}")

@bot.message_handler(commands=['name'])
def name_cmd(message):
    name = message.from_user.first_name or "دوست من"
    bot.send_message(message.chat.id, f"سلام {name}")

# --- Start Bot ---
bot.delete_webhook()
bot.polling(none_stop=True, interval=0)
