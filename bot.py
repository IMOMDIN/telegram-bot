import telebot
import os
import time

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, "Бот работает стабильно и бесплатно.")

# Работаем ограниченное время, чтобы GitHub Actions не зависал
start_time = time.time()
while time.time() - start_time < 55:
    try:
        bot.polling(none_stop=True, interval=1, timeout=20)
    except Exception:
        time.sleep(5)