import time
import telebot
token = "5785032666:AAHmweiukEUklqPhvcEjFw-q4IGZvJiehNU"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Введи /start для начала.")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, я телеграм-бот для знакомств. Я помогу тебе найти друга или подругу.")
    #time.sleep(0.5)
    #bot.send_message(message.chat.id, "Давай начнём. Кто ты?")
async def send_welcome(types):
    kb = [
        [
            types.KeyboardButton(text="Парень"),
            types.KeyboardButton(text="Девушка")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await types.message.reply(reply_markup=keyboard)
    bot.send_message(message.chat.id, "Давай начнём. Кто ты?")

bot.infinity_polling()