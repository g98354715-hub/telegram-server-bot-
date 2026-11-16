import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "Assalomu alaykum! 👋\n"
        " CHAT BOT ga xush kelibsiz! 🤖"
    )

@bot.message_handler(func=lambda message: True)
def reply(message):
    bot.reply_to(message, "Xabaringiz qabul qilindi! 😊")

bot.infinity_polling()
