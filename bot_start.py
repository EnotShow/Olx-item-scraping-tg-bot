import telebot
from telebot import types


def get_token_from_file():
    with open('token.txt', encoding='UTF-8') as file:
        bot_token = file.readlines()
        bot_token = ''.join(bot_token)
        return bot_token


def telegram_bot():
    bot = telebot.TeleBot(get_token_from_file())

    @bot.message_handler(commands=['start'])
    def start_message(message):
        markup_inline = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton('Start', callback_data='/start_scraping')
        markup_inline.add(button)

        bot.send_message(message.chat.id, "Нажми 'Start' что бы начать", reply_markup=markup_inline)

    @bot.callback_query_handler(func=lambda call: True)
    def result_to_user(call):
        bot.send_message(call.message.chat.id, 'Начал парсинг')
        while True:
            bot.send_message(call.message.chat.id, aggregator())

    bot.polling()


if __name__ == '__main__':
    from main import *

    telegram_bot()
