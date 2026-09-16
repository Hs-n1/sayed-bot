import os
from threading import Thread
from flask import Flask
from telethon import TelegramClient, events

# إعداد خادم الويب الوهمي لإرضاء سيرفر Render
app = Flask('')


@app.route('/')
def home():
  return "Sayed UserBot is Alive and Running!"


def run_web():
  app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))


# بيانات التطبيق الخاصة بك
API_ID = 38922466
API_HASH = "01c78598b98912f64d5e1f19d8775008"
PHONE_NUMBER = "+9647853349876"

# عبارة الرد التلقائي المزخرفة
REPLY_MESSAGE = (
    "▂▃▅▆▇ 🌟 أهلاً بك 🌟 ▇▆▅▃▂\n\nعذراً، لسنا متاحين الآن...\nولكن\n✨ [ سوف يتم"
    ' الرد عليك بواسطة "السيد" ] ✨\n\nيرجى ترك رسالتك وسنقوم بالرد قريباً ⏳👇'
)

# إنشاء جلسة للـ UserBot
client = TelegramClient("sayed_session", API_ID, API_HASH)


@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def auto_reply(event):
  if event.sender and event.sender.bot:
    return
  try:
    await event.reply(REPLY_MESSAGE)
  except Exception as e:
    print(f"Error sending auto-reply: {e}")


def main():
  # تشغيل خادم الويب في الخلفية
  t = Thread(target=run_web)
  t.start()

  print("Starting Telegram UserBot for Sayed...")
  client.start(phone=PHONE_NUMBER)
  print("UserBot is running and listening for incoming messages...")
  client.run_until_disconnected()


if __name__ == "__main__":
  main()
