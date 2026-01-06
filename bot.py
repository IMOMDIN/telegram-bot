import telebot
import os
import time

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

users = set()

@bot.message_handler(commands=['start'])
def start(msg):
    users.add(msg.chat.id)
    bot.send_message(msg.chat.id, "Привет. Я рабочий Telegram-бот.")

@bot.message_handler(commands=['stats'])
def stats(msg):
    bot.send_message(msg.chat.id, f"Пользователей: {len(users)}")

@bot.message_handler(func=lambda m: True)
def echo(msg):
    bot.send_message(msg.chat.id, f"Ты написал: {msg.text}")

start_time = time.time()
while time.time() - start_time < 55:
    try:
        bot.polling(none_stop=True, interval=1, timeout=20)
    except Exception:
        time.sleep(5)