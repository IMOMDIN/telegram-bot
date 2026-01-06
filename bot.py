import telebot
import os

TOKEN = os.getenv("8429213122:AAGTyhBjK1lmtFaYqHDG3OvrHOp3dU8UWfE")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бот работает.")

bot.infinity_polling()