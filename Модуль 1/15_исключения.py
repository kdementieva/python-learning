#Задание 1
# a = input('Введите первое значение: ')
# b = input('Введите второе значение: ')
# try:
#     print(int(a) + int(b))
# except:
#     print(a + b)


#Задание 2
import re

password = input('Введите пароль: ')
try:
    pattern = re.compile(r'^\d+$') #добавляем в переменную регулярное выражение
    if password == '':
        raise ValueError('Вы ввели пустой пароль') #вызываем исключение с сообщением
    if pattern.search(password):
        raise ValueError('Ваш пароль состоит только из цифр')
except ValueError as e:
    print(e)
else:
    print('Требования к паролю соблюдены')


