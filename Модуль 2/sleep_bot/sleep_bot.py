import os
import telebot
import json
from datetime import datetime
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(current_dir, "dev.env"))

bot = telebot.TeleBot(os.getenv('TOKEN'))

SLEEP = 'sleep'
WAKE = 'wake'
QUALITY = 'quality'
NOTES = 'notes'
START_MESSAGE = f'Привет, я буду помогать тебе отслеживать параметры сна. Используй команды /{SLEEP}, /{WAKE}, /{QUALITY} и /{NOTES}.'
SLEEP_MESSAGE = f'Спокойной ночи! Не забудь сообщить мне, когда проснешься командой /{WAKE}.'
NO_SLEEP = f'Я не вижу, что ты сообщил(а) мне о начале сна. Используй команду /{SLEEP}.'
WAKE_MESSAGE = 'Доброе утро! Ты спал(а) {hours} часов и {minutes} минут. `' + f'Не забудь оценить качество сна командой /{QUALITY} и оставить заметки командой /{NOTES}.'
NO_DATA = f'Не вижу записи сна, которую ты хочешь оценить. Используй команду /sleep, чтобы начать запись.'
QUAL_MESSAGE = 'Спасибо за оценку качества сна!'
NOTE_MESSAGE = 'Заметка успешно сохранена!'
EMPTY = 'Пожалуйста, введи данные!'

def save_data(data):
    with open('sleep_data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_data():
    try:
        with open('sleep_data.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

data = load_data()

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, text=START_MESSAGE)

@bot.message_handler(commands=[SLEEP])
def sleep_mess(m):
    user_id = m.from_user.id
    sleep_time = datetime.fromtimestamp(m.date)
    if user_id not in data:
        data[user_id] = {}
    data[user_id]['sleep_time'] = sleep_time.isoformat()
    save_data(data)
    bot.reply_to(m, text=SLEEP_MESSAGE)

@bot.message_handler(commands=[WAKE])
def wake_mess(m):
    user_id = m.from_user.id
    if user_id not in data or 'sleep_time' not in data[user_id]:
        return bot.send_message(m.chat.id, text=NO_SLEEP)

    wake_time = datetime.fromtimestamp(m.date)
    sleep_time = datetime.fromisoformat(data[user_id]['sleep_time'])

    time_difference = (wake_time - sleep_time).total_seconds()
    hours = int(time_difference // 3600)
    minutes = int((time_difference % 3600) // 60)

    data[user_id] = {'timedelta': time_difference}
    save_data(data)

    bot.reply_to(m, text=WAKE_MESSAGE.format(hours=hours, minutes=minutes))

@bot.message_handler(commands=[QUALITY])
def qual_mess(m):
    user_id = m.from_user.id
    if user_id not in data or 'timedelta' not in data[user_id]:
        return bot.send_message(m.chat.id, text=NO_DATA)
    ans = m.text.split(maxsplit=1)
    if len(ans) < 2:
        return bot.send_message(m.chat.id, text=EMPTY)
    
    quality = ans[1]
    data[user_id]['quality'] = quality
    save_data(data)

    bot.reply_to(m, text=QUAL_MESSAGE)

@bot.message_handler(commands=[NOTES])
def note_mess(m):
    user_id = m.from_user.id
    if user_id not in data or 'timedelta' not in data[user_id]:
        return bot.send_message(m.chat.id, text=NO_DATA)
    ans = m.text.split(maxsplit=1)
    if len(ans) < 2:
        return bot.send_message(m.chat.id, text=EMPTY)

    note = ans[1]
    data[user_id]['notes'] = note
    save_data(data)

    bot.reply_to(m, text=NOTE_MESSAGE)

if __name__ == "__main__":
    load_data()
    bot.polling(none_stop=True, interval=0)
