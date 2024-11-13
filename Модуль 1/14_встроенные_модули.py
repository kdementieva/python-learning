#Генератор случайных паролей
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password =''.join(random.choice(characters) for _ in range(length))
    return password

print(generate_password(10))

#Работа с датами
import datetime

def count_years (birthday):
    now = datetime.datetime.today()
    years = now.year - birthday.year
    if (now.month, now.day) < (birthday.month, birthday.day):
        years -= 1
    return years

birthday = input('Введите дату рождения в формате ДД.ММ.ГГГГ: ')
day, month, year = map(int, birthday.split('.'))
birthday = datetime.datetime(year, month, day)
print(f'Вам сейчас {count_years(birthday)} лет')

#Статистика слов в тексте
import collections
import re

def words_statistics(s):
    s = s.lower()
    words = re.findall(r'\b\w+\b', s)  #регулярное выражение для извлечения слов
    count = collections.Counter(words)
    sorted_count = count.most_common()
    return sorted_count

print(words_statistics('Сегодня отличная погода. Я решил пойти на прогулку в парк. В парке много людей, все наслаждаются тёплым осенним днём. Я взял с собой книгу и сел на скамейку под деревом. Ветерок тихо шелестел листьями, создавая спокойную атмосферу. Прохожие проходили мимо, некоторые гуляли с собаками, а кто-то катался на велосипеде. Я решил провести здесь несколько часов, наслаждаясь тишиной и природой. Вскоре ко мне присоединились друзья, и мы начали обсуждать планы на выходные.'))