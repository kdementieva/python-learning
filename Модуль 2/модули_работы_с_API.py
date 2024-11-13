import os
import telebot
import wikipedia

import warnings
from bs4 import GuessedAtParserWarning

# Код, который отключает конкретное предупреждение о парсере
# пробовала установить парсер html.parser, но и так выскакивало

warnings.filterwarnings("ignore", category=GuessedAtParserWarning)

bot = telebot.TeleBot(os.getenv('token'))

START_MESSAGE = '''Привет! Я бот для поиска информации в Википедии.\n
Выбери язык, на котором хочешь работать: /ru для русского или /en для английского.\n
После выбора языка просто отправь мне запрос, и я найду информацию на Википедии!'''
RU = 'Отлично! Введи запрос!'
EN = 'Alright! Enter your query!'
PAGE_ERROR_RU = 'По вашему запросу ничего не найдено.'
PAGE_ERROR_EN = 'Nothing found matching your query.'
DISAMBIGUATION_RU = 'Ваш запрос имеет несколько значений: {}.\nПопробуйте еще раз.'
DISAMBIGUATION_EN = 'Your query has multiple meanings: {}.\nTry again.'
WARN_MESS = 'Сначала выбери язык с помощью команды /ru или /en.'

current_lang = None

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, text = START_MESSAGE)


@bot.message_handler(commands = ['ru', 'en'])
def lang(mess):
    global current_lang
    if mess.text == '/ru':
        wikipedia.set_lang('ru')
        bot.send_message(mess.chat.id, text = RU)
        current_lang = 'ru'
    elif mess.text == '/en':
        wikipedia.set_lang('en')
        bot.send_message(mess.chat.id, text = EN)
        current_lang = 'en'

@bot.message_handler(func=lambda message: True)
def get_article(message):
    global current_lang

    if current_lang is None:
        bot.send_message(message.chat.id, text = WARN_MESS)
        return

    try:
        ans = wikipedia.summary(message.text)
        bot.reply_to(message, ans)
    except wikipedia.exceptions.PageError:
        if current_lang == 'ru':
            bot.send_message(message.chat.id, text = PAGE_ERROR_RU)
        elif current_lang == 'en':
            bot.send_message(message.chat.id, text = PAGE_ERROR_EN)
    except wikipedia.exceptions.DisambiguationError as e:
        if current_lang == 'ru':
            bot.send_message(message.chat.id, text = DISAMBIGUATION_RU.format(', '.join(e.options[:5])))
        elif current_lang == 'en':
            bot.send_message(message.chat.id, text = DISAMBIGUATION_EN.format(', '.join(e.options[:5])))

bot.polling(none_stop=True, interval=0)


