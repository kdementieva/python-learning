#1
a = float(input('Введите число, проверьте положительное ли оно: '))

if a > 0:
    print('True')
else:
    print('False')

#2
b = float(input('Введите число, проверьте нечетное ли оно: '))

if b % 2 == 0:
    print('False')
else:
    print('True')

#3
a = input('Введите число, чтобы проверить последнюю цифру: ')
l = int(a[-1])

if l == 3:
    print('True')
else:
    print('False')

#4
x = float(input('Введите число, чтобы проверить принадлежит ли оно промежутку [0,15]: '))

if x>=0 and x<=15:
    print('True')
else:
    print('False')

#5
x = input('Введите число: ')
l = int(x[-1])

if float(x) % 3 == 0 and l == 5:
    print('True')
else:
    print('False')

#6
first = float(input('Введите первое число: '))
second = float(input('Введите второе число: '))

if first > second:
    print('Первое больше ')
elif second > first:
    print('Второе больше')
else:
    print('Равны')

#7
s = input('Введите три целых числа: ')
l = s.split()

first = int(l[0])
second = int(l[1])
third = int(l[2])
number = 0

if first % 2 == 0:
    number += 1
if second % 2 == 0:
    number += 1
if third % 2 == 0:
    number += 1

if number == 0:
    print('Нет четных чисел')
elif number == 1:
    print('Одно число четное')
elif number == 2:
    print('Два числа четные')
else:
    print('Все числа четные')

#8
month = { '1': 'январь',
          '2': 'февраль',
          '3': 'март',
          '4': 'апрель',
          '5': 'май',
          '6': 'июнь',
          '7': 'июль',
          '8': 'август',
          '9': 'сентябрь',
          '10': 'октябрь',
          '11': 'ноябрь',
          '12': 'декабрь'}
num = input('Введите номер месяца (от 1 до 12): ')
print(month[num])

#9
num = input('Введите трехзначное число: ')
l = list(num)

first = int(l[0])
second = int(l[1])
third = int(l[2])

if (first + second + third) % 3 == 0:
    print('Да')
else:
    print('Нет')

#10
year = int(input('Введите год: '))

if year % 400 == 0:
    print('високосный')
elif year % 4 == 0 and year % 100 != 0:
    print('високосный')
else:
    print('невисокосный')

#11
x = input('Введите положительное число х (х<1000): ')
l = list(x)

if len(l) == 1:
    print('однозначное')
elif len(l) == 2:
    print('двузначное')
else:
    print('трехзначное')

#12
s = input('Введите два числа: ')
l = s.split()

operation = int(input('Введите арифметическую операцию ( "1" - сложение, "2" - вычитание, "3" - умножение, "4" - деление): '))

if operation == 1:
    print(int(l[0]) + int(l[1]))
elif operation == 2:
    print(int(l[0]) - int(l[1]))
elif operation == 3:
    print(int(l[0]) * int(l[1]))
else:
    print(int(l[0]) / int(l[1]))