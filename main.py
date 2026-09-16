import os
from telethon import TelegramClient, events

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
  # تجاهل الرسائل من بوتات أخرى أو الرسائل المحذولة
  if event.sender and event.sender.bot:
    return

  try:
    # الرد على الشخص بالعبارة المزخرفة
    await event.reply(REPLY_MESSAGE)
  except Exception as e:
    print(f"Error sending auto-reply: {e}")


def main():
  print("Starting Telegram UserBot for Sayed...")
  # بدء التشغيل وربط الحساب برقم الهاتف
  client.start(phone=PHONE_NUMBER)
  print("UserBot is running and listening for incoming messages...")
  client.run_until_disconnected()


if __name__ == "__main__":
  main()
