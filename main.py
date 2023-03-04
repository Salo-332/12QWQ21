import time
import telebot

token = "5785032666:AAHmweiukEUklqPhvcEjFw-q4IGZvJiehNU"

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, я телеграм-бот для поиска друзей в школе №1561.")
        time.sleep(0.5)
        keyboard = telebot.types.InlineKeyboardMarkup()
        button1 = telebot.types.InlineKeyboardButton(text="Парень", callback_data="button1")
        button2 = telebot.types.InlineKeyboardButton(text="Девушка", callback_data="button2")
        keyboard.row(button1, button2)
        bot.send_message(message.from_user.id, "Давай начнём. Кто ты?", reply_markup=keyboard)


    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Тыкни /start")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Тыкни /help")


@bot.callback_query_handler(func=lambda call: call.data in ["button1", "button2"])
def callback_function1(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button3 = telebot.types.InlineKeyboardButton(text="1", callback_data="button3")
    button4 = telebot.types.InlineKeyboardButton(text="2", callback_data="button4")
    button5 = telebot.types.InlineKeyboardButton(text="3", callback_data="button5")
    button6 = telebot.types.InlineKeyboardButton(text="11", callback_data="button6")
    keyboard.row(button3, button4, button5, button6)
    bot.send_message(message.from_user.id, "Из какого ты корпуса?", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data in ["button3", "button4", "button5", "button6"])
def callback_function2(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button7 = telebot.types.InlineKeyboardButton(text="12", callback_data="button7")
    button8 = telebot.types.InlineKeyboardButton(text="13", callback_data="button8")
    button9 = telebot.types.InlineKeyboardButton(text="14", callback_data="button9")
    button10 = telebot.types.InlineKeyboardButton(text="15", callback_data="button10")
    button11 = telebot.types.InlineKeyboardButton(text="16", callback_data="button11")
    button12 = telebot.types.InlineKeyboardButton(text="17", callback_data="button12")
    keyboard.row(button7, button8, button9)
    keyboard.row(button10, button11, button12)
    bot.send_message(message.from_user.id, "Сколько тебе лет?", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data in ["button7", "button8", "button9", "button10", "button11", "button12"])
def callback_function3(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button13 = telebot.types.InlineKeyboardButton(text="ПРИМЕР1", callback_data="button13")
    button14 = telebot.types.InlineKeyboardButton(text="ПРИМЕР2", callback_data="button14")
    button15 = telebot.types.InlineKeyboardButton(text="ПРИМЕР3", callback_data="button15")
    button16 = telebot.types.InlineKeyboardButton(text="ПРИМЕР4", callback_data="button16")
    button17 = telebot.types.InlineKeyboardButton(text="ПРИМЕР5", callback_data="button17")
    button18 = telebot.types.InlineKeyboardButton(text="ПРИМЕР6", callback_data="button18")
    keyboard.row(button13, button14, button15)
    keyboard.row(button16, button17, button18)
    bot.send_message(message.from_user.id, "Выберите ваши интересы из списка.", reply_markup=keyboard)

#def korpus(message):
    #chat_id = message.chat.id
    #answer = bot.send_message(chat_id, "")


bot.infinity_polling()
