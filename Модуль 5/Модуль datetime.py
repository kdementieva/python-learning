import datetime as dt
import calendar

def count_diff (date):
    now = dt.datetime.now()
    difference = now - date
    days = difference.days
    seconds = difference.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return days, hours, minutes

now = dt.datetime.now()
print('Текущая дата и время:', now)
print('Текущий день недели: ', now.strftime('%A'))
if calendar.isleap(now.year):
    print('Текущий год високосный.')
else:
    print('Текущий год не високосный.')

date_ = input('Введите дату в формате ГГГГ-ММ-ДД: ')
year, month, day= map(int, date_.split('-'))
date_ = dt.datetime(year, month, day)
days, hours, minutes = count_diff(date_)
print(f'Разница с датой {date_}: {days} дней, {hours} часов, {minutes} минут')
