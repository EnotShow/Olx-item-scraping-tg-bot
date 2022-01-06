import telebot
from telebot import types

from data_importers import get_token_from_file


def telegram_bot():
    bot = telebot.TeleBot(get_token_from_file())

    @bot.message_handler(commands=['start'])
    def start_message(message):
        markup_inline = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton('Start', callback_data='/start_scraping')
        markup_inline.add(button)

        bot.send_message(
            message.chat.id,
            "Нажми 'Start' что бы начать",
            reply_markup=markup_inline
        )

    @bot.callback_query_handler(func=lambda call: True)
    def sender(call):
        bot.send_message(
            call.message.chat.id,
            "Начал парсинг"
        )
        while True:
            bot_message = sent_to_user
            bot.send_message(call.message.chat.id, bot_message())

    @bot.message_handler(commands=['start_scraping'])
    def sender_to(message):
        bot.send_message(
            message.chat.id,
            "Начал парсинг"
        )
        while True:
            bot_message = sent_to_user
            bot.send_message(message.chat.id, bot_message())

    bot.polling()


if __name__ == '__main__':
    from main import *

    telegram_bot()
