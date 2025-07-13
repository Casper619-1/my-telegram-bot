import telebot
import random
import datetime

import os
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Создаем бота
bot = telebot.TeleBot(BOT_TOKEN)

# Список шуток для бота
jokes = [
    "Почему программисты не любят природу? Слишком много багов! 🐛",
    "Что такое рекурсия? Смотри определение рекурсии 🔄",
    "Почему Java-разработчики носят очки? Потому что не видят C# 😎",
    "10 типов людей: те, кто понимает двоичную систему, и те, кто нет 😄",
    "Как называется собака программиста? Лайка! 🐕"
]

# Список полезных фактов
facts = [
    "🧠 Человеческий мозг потребляет примерно 20% всей энергии тела",
    "🐙 У осьминога три сердца и голубая кровь",
    "🌍 Один день на Венере длится дольше, чем год на Венере",
    "🐝 Пчелы могут считать до четырех",
    "🎵 Сердце кита бьется так медленно, что человек мог бы проползти через его артерии"
]

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Я простой бот-помощник. Вот что я умею:\n\n"
        "🔹 /help - показать все команды\n"
        "🔹 /joke - рассказать шутку\n"
        "🔹 /fact - интересный факт\n"
        "🔹 /time - показать время\n"
        "🔹 /weather - узнать 'погоду' (шутка)\n"
        "🔹 /roll - бросить кубик\n\n"
        "Также можете просто написать мне что-нибудь! 😊"
    )

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(
        message.chat.id,
        "📝 Список доступных команд:\n\n"
        "🔹 /start - начать общение\n"
        "🔹 /help - показать это сообщение\n"
        "🔹 /joke - случайная шутка\n"
        "🔹 /fact - интересный факт\n"
        "🔹 /time - текущее время\n"
        "🔹 /weather - 'прогноз погоды'\n"
        "🔹 /roll - бросить кубик (1-6)\n\n"
        "Просто напишите мне что-нибудь, и я отвечу! 💬"
    )

# Обработчик команды /joke
@bot.message_handler(commands=['joke'])
def joke_message(message):
    random_joke = random.choice(jokes)
    bot.send_message(message.chat.id, f"😄 {random_joke}")

# Обработчик команды /fact
@bot.message_handler(commands=['fact'])
def fact_message(message):
    random_fact = random.choice(facts)
    bot.send_message(message.chat.id, f"💡 Интересный факт:\n{random_fact}")

# Обработчик команды /time
@bot.message_handler(commands=['time'])
def time_message(message):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    bot.send_message(
        message.chat.id,
        f"🕐 Текущее время: {current_time}\n"
        f"📅 Дата: {current_date}"
    )

# Обработчик команды /weather
@bot.message_handler(commands=['weather'])
def weather_message(message):
    weather_variants = [
        "☀️ Солнечно и тепло! Отличный день для прогулки",
        "🌧️ Дождливо... Лучше взять зонт",
        "❄️ Снежно и морозно! Одевайтесь теплее",
        "🌤️ Переменная облачность, в принципе неплохо",
        "🌪️ Ураган! Лучше остаться дома (шучу)",
        "🌈 После дождичка в четверг - появилась радуга!"
    ]
    fake_weather = random.choice(weather_variants)
    bot.send_message(
        message.chat.id,
        f"🌍 Прогноз погоды:\n{fake_weather}\n\n"
        "💡 Это шуточный прогноз! Для реальной погоды используйте специальные приложения 😊"
    )

# Обработчик команды /roll
@bot.message_handler(commands=['roll'])
def roll_message(message):
    dice_result = random.randint(1, 6)
    dice_emoji = ["", "⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
    bot.send_message(
        message.chat.id,
        f"🎲 Кубик брошен!\n"
        f"Результат: {dice_emoji[dice_result]} ({dice_result})"
    )

# Обработчик всех остальных сообщений
@bot.message_handler(content_types=['text'])
def text_message(message):
    user_text = message.text.lower()
    
    # Простые ответы на популярные фразы
    responses = {
        "привет": "Привет! 👋 Как дела?",
        "пока": "До свидания! 👋 Было приятно пообщаться!",
        "как дела": "У меня всё отлично! 😊 Готов помочь вам!",
        "спасибо": "Пожалуйста! 😊 Всегда рад помочь!",
        "что умеешь": "Я умею шутить, рассказывать факты, показывать время и многое другое! Напишите /help для списка команд",
        "кто ты": "Я простой бот-помощник! 🤖 Создан для того, чтобы развлекать и помогать",
    }
    
    # Проверяем, есть ли ответ на сообщение пользователя
    for key, response in responses.items():
        if key in user_text:
            bot.send_message(message.chat.id, response)
            return
    
    # Если нет готового ответа, отвечаем дружелюбно
    bot.send_message(
        message.chat.id,
        f"Интересно! 🤔 Вы написали: '{message.text}'\n\n"
        "Я пока не знаю, как на это ответить, но вы можете:\n"
        "• Написать /help для списка команд\n"
        "• Попробовать /joke для шутки\n"
        "• Или просто поболтать со мной! 😊"
    )

# Обработчик ошибок
@bot.message_handler(content_types=['photo', 'video', 'audio', 'document', 'sticker'])
def media_message(message):
    media_types = {
        'photo': 'фотографию 📸',
        'video': 'видео 🎥',
        'audio': 'аудио 🎵',
        'document': 'документ 📄',
        'sticker': 'стикер 😊'
    }
    
    media_type = media_types.get(message.content_type, 'файл')
    bot.send_message(
        message.chat.id,
        f"Спасибо за {media_type}! 😊\n\n"
        "Я пока не умею обрабатывать медиафайлы, но могу:\n"
        "• Ответить на текстовые сообщения\n"
        "• Выполнить команды (напишите /help)\n"
        "• Поболтать с вами! 💬"
    )

# Функция для запуска бота
def main():
    print("🤖 Бот запущен!")
    print("📝 Для остановки нажмите Ctrl+C")
    
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        print("🔄 Перезапуск бота...")
        main()

# Запуск бота
if __name__ == "__main__":
    main()