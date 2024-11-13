import os
import telebot
from datetime import datetime

bot = telebot.TeleBot(os.getenv('token'))

SLEEP = 'sleep'
WAKE = 'wake'
QUALITY = 'quality'
NOTES = 'notes'
START_MESSAGE = f'Привет, я буду помогать тебе отслеживать параметры сна. Используй команды /{SLEEP}, /{WAKE}, /{QUALITY} и /{NOTES}.'
SLEEP_MESSAGE = f'Спокойной ночи! Не забудь сообщить мне, когда проснешься командой /{WAKE}.'
NO_SLEEP = f'Я не вижу, что ты сообщил(а) мне о начале сна. Используй команду /{SLEEP}.'
WAKE_MESSAGE = 'Доброе утро! Ты проспал(а) около {sleep_hours} часов. `' + f'Не забудь оценить качество сна командой /{QUALITY} и оставить заметки командой /{NOTES}.'
NO_DATA = f'Не вижу записи сна, которую ты хочешь оценить. Используй команду /{SLEEP}, чтобы начать запись.'
QUAL_MESSAGE = 'Спасибо за оценку качества сна!'
NOTE_MESSAGE = 'Заметка успешно сохранена!'
EMPTY = 'Пожалуйста, введи данные!'

data = {}


@bot.message_handler(commands = ['start'])
def start(m):
    bot.send_message(m.chat.id, text = START_MESSAGE)


@bot.message_handler(commands = [SLEEP])
def sleep_mess(m):
    user_id = m.from_user.id
    sleep_time = datetime.fromtimestamp(m.date)

    if user_id not in data:
        data[user_id] = {}

    data[user_id]['sleep_time'] = sleep_time
    bot.reply_to(m, text = SLEEP_MESSAGE)

@bot.message_handler(commands = [WAKE])
def wake_mess(m):
    user_id = m.from_user.id
    if user_id not in data or 'sleep_time' not in data[user_id]:
        return bot.send_message(m.chat.id, text = NO_SLEEP)
    wake_time = datetime.fromtimestamp(m.date)
    sleep_time = data[user_id]['sleep_time']
    timedelta = wake_time - sleep_time
    sleep_hours = timedelta.total_seconds() / 3600 # в часах
    data[user_id]['timedelta'] = timedelta
    bot.reply_to(m, text = WAKE_MESSAGE.format(sleep_hours = sleep_hours))

@bot.message_handler(commands = [QUALITY])
def qual_mess(m):
    user_id = m.from_user.id
    if user_id not in data or 'timedelta' not in data[user_id]:
        return bot.send_message(m.chat.id, text = NO_DATA)
    ans = m.text.split(maxsplit=1)
    if len(ans) < 2:
        return bot.send_message(m.chat.id, text = EMPTY)
    quality = ans[1]
    data[user_id]['quality'] = quality
    bot.reply_to(m, text = QUAL_MESSAGE)

@bot.message_handler(commands = [NOTES])
def note_mess(m):
    user_id = m.from_user.id
    if user_id not in data or 'timedelta' not in data[user_id]:
        bot.send_message(m.chat.id, text = NO_DATA)
        return
    ans = m.text.split(maxsplit=1)
    if len(ans) < 2:
        return bot.send_message(m.chat.id, text=EMPTY)
    note = ans[1]
    data[user_id]['notes'] = note
    bot.reply_to(m, text = NOTE_MESSAGE)



bot.polling(none_stop=True, interval=0)