day = int(input('Введите целое количество дней '))
hour = day * 24
minute = hour * 60
second = minute * 60
info = f'{day} суток = {hour} часов = {minute} минут = {second} секунд'
print(info)