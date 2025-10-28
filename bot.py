import telebot
import os
from flask import Flask

# 🔑 Твій токен (вкажи свій у Koyeb -> Environment Variables -> TELEGRAM_TOKEN)
TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# 🖐️ Привітання нових учасників
@bot.message_handler(content_types=['new_chat_members'])
def greet_new_member(message):
    for new_member in message.new_chat_members:
        mention = f"@{new_member.username}" if new_member.username else new_member.first_name
        text = (
            f"👋 Ласкаво просимо у нашу дружню родину, {mention}!\n\n"
            f"Ознайомся з гілками — там є важлива інформація 😎\n"
            f"Закидай фотку свого VAG, хай всі оцінять 🚗💨😉"
        )
        bot.send_message(message.chat.id, text)

# 🌐 Flask-сервер для стабільності
@app.route('/')
def home():
    return "Бот працює стабільно 🚀"

if __name__ == "__main__":
    print("✅ Бот запущений і працює 24/7...")
    from threading import Thread
    Thread(target=lambda: bot.polling(none_stop=True, interval=0, timeout=20)).start()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
