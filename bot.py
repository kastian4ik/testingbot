import telebot
import os
from flask import Flask
import time
from threading import Thread

# 🔑 Підхоплюємо токен з Environment Variable
TOKEN = os.environ.get("TELEGRAM_TOKEN")

# Перевірка токена перед стартом
if not TOKEN:
    raise ValueError("❌ TELEGRAM_TOKEN не знайдено. Перевір Environment Variables на Koyeb!")

# Створюємо бота з більшим таймаутом
bot = telebot.TeleBot(TOKEN, request_timeout=60)
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

# 🌐 Flask-сервер для підтримки health check
@app.route('/')
def home():
    return "Бот працює стабільно 🚀"

# Функція запуску бота з нескінченним опитуванням та обробкою помилок
def run_bot():
    while True:
        try:
            bot.infinity_polling()
        except Exception as e:
            print(f"⚠️ Помилка: {e}. Перезапуск через 5 секунд...")
            time.sleep(5)

if __name__ == "__main__":
    print("✅ Бот запущений і працює 24/7...")
    # Запускаємо бота у окремому потоці
    Thread(target=run_bot).start()
    # Запускаємо Flask для Koyeb
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
