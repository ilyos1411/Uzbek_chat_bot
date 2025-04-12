import os
import telebot
from dotenv import load_dotenv

# .env faylni yuklash
load_dotenv()

# Tokenlarni olish
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Salom! Men sizning Telegram botman. Savollaringizni yuboring!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Siz yuborgan matn: " + message.text)

bot.infinity_polling()
