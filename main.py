import os
from flask import Flask, request
import telebot

TOKEN = '8918468809:AAEcdcGqm0sYojBZAvoDwv0YHugXqo8M-jM'
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

welcome_message = """ ▂▃▅▆▇ 🌟 أهلاً بك 🌟 ▇▆▅▃▂ 

عذراً، لسنا متاحين الآن... 
ولكن 
✨ [ سوف يتم الرد عليك بواسطة "السيد" ] ✨

يرجى ترك رسالتك وسنقوم بالرد قريباً ⏳👇"""


@bot.message_handler(func=lambda message: True)
def send_welcome(message):
  bot.reply_to(message, welcome_message)


@app.route('/')
def home():
  return 'System is active and running 24/7!'


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  import threading

  t = threading.Thread(target=bot.infinity_polling)
  t.daemon = True
  t.start()

  app.run(host='0.0.0.0', port=port)

