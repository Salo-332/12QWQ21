import time
import telebot
token = "5785032666:AAHmweiukEUklqPhvcEjFw-q4IGZvJiehNU"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def start_message(message):

    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, я телеграм-бот для знакомств. Я помогу тебе найти друга или подругу.")
        time.sleep(0.5)
        #bot.send_message(message.from_user.id, "Давай начнём. Кто ты?")
        keyboard = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Парень", callback_data="button1")
        button2 = telebot.types.InlineKeyboardButton(text="Девушка", callback_data="button2")
        keyboard.row(button1, button2)
        bot.send_message(message.from_user.id, "Давай начнём. Кто ты?", reply_markup=keyboard)


    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Тыкни /start")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Тыкни /help")

@bot.callback_query_handler(func=lambda call: call.data == "button1")
def callback_function1(callback_obj):
    


bot.infinity_polling()
