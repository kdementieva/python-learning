import os
import telebot
import sqlite3
from datetime import datetime
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(current_dir, "dev.env"))

bot = telebot.TeleBot(os.getenv('TOKEN'))

def create_db_if_not_exists():
    conn = sqlite3.connect('sleep_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sleep_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        sleep_time DATETIME,
        wake_time DATETIME,
        sleep_quality INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        sleep_record_id INTEGER,
        FOREIGN KEY(sleep_record_id) REFERENCES sleep_records(id)
    );
    ''')
    conn.commit()
    conn.close()

create_db_if_not_exists()

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

def get_db_connection():
    conn = sqlite3.connect('sleep_bot.db', check_same_thread=False)
    conn.isolation_level = None
    return conn

def is_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM users WHERE id = (?)', (user_id,))
    if cursor.fetchone() is None:
        conn.close()
        return False
    conn.close()
    return True

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, text=START_MESSAGE)

@bot.message_handler(commands=[SLEEP])
def sleep_mess(m):
    user_id = m.from_user.id
    username = m.from_user.username
    sleep_time = datetime.fromtimestamp(m.date)
    sleep_time_str = sleep_time.isoformat()
    conn = get_db_connection()
    cursor = conn.cursor()
    if not is_user(user_id):
        conn.execute('INSERT INTO users(id, name) VALUES(?, ?)', (user_id, username))
        conn.commit()
    cursor.execute('INSERT INTO sleep_records (user_id, sleep_time) VALUES (?, ?)', (user_id, sleep_time_str))
    conn.commit()
    conn.close()
    bot.reply_to(m, text=SLEEP_MESSAGE)

@bot.message_handler(commands=[WAKE])
def wake_mess(m):
    user_id = m.from_user.id
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT sleep_time FROM sleep_records WHERE user_id = (?)', (user_id,))
    record = cursor.fetchone()

    if not is_user(user_id) and record is None:
        return bot.send_message(m.chat.id, text=NO_SLEEP)
    
    wake_time = datetime.fromtimestamp(m.date)
    wake_time_str = wake_time.isoformat()
    sleep_time = datetime.fromisoformat(record[0])
    cursor.execute('UPDATE sleep_records SET wake_time = (?) WHERE user_id = (?) AND sleep_time = (?)', (wake_time_str, user_id, sleep_time))
    conn.close()

    time_difference = (wake_time - sleep_time).total_seconds()
    hours = int(time_difference // 3600)
    minutes = int((time_difference % 3600) // 60)

    bot.reply_to(m, text=WAKE_MESSAGE.format(hours=hours, minutes=minutes))

@bot.message_handler(commands=[QUALITY])
def qual_mess(m):
    user_id = m.from_user.id
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT wake_time FROM sleep_records WHERE user_id = (?)', (user_id,))
    record = cursor.fetchone()
    if not is_user(user_id) or record is None:
        return bot.send_message(m.chat.id, text=NO_DATA)
    ans = m.text.split(maxsplit=1)
    if len(ans) < 2:
        return bot.send_message(m.chat.id, text=EMPTY)
    
    quality = ans[1]
    cursor.execute('UPDATE sleep_records SET sleep_quality = (?) WHERE user_id = (?) AND wake_time = (?)', (quality, user_id, record[0]))
    conn.commit()
    conn.close()

    bot.reply_to(m, text=QUAL_MESSAGE)

@bot.message_handler(commands=[NOTES])
def note_mess(m):
    user_id = m.from_user.id
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM sleep_records WHERE user_id = (?) AND wake_time IS NOT NULL', (user_id,))
    record = cursor.fetchone()
    if not is_user(user_id) or record is None:
        return bot.send_message(m.chat.id, text=NO_DATA)
    ans = m.text.split(maxsplit=1)
    if len(ans) < 2:
        return bot.send_message(m.chat.id, text=EMPTY)

    note = ans[1]
    cursor.execute('INSERT INTO notes (text, sleep_record_id) VALUES (?, ?)', (note, record[0]))
    conn.commit()
    conn.close()

    bot.reply_to(m, text=NOTE_MESSAGE)


bot.polling(none_stop=True, interval=0)
