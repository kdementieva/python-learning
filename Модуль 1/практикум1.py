#1
name = input('Напишите имя: ')
print('Привет, ' + name)

#2
str1 = input('Введите первую строку: ')
str2 = input('Введите вторую строку: ')
str3 = input('Введите третью строку: ')

print(str3)
print(str2)
print(str1)

#3
a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))
c = (a + b) / 2
print('Среднее арифметическое: ' + str(int(c)))

#4
farh = float(input('Укажите значение по шкале Фаренгейта: '))
c = 5/9*(farh-32)
rndc = round(c, 2)
print('По Цельсия соответствует ' + str(rndc) + ' градусов')

#5
a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))
c = int(input('Введите третье целое число: '))
maximum = max(a, b, c)
minimum = min(a, b, c)
middle = (a + b + c) - maximum - minimum

print(maximum, middle, minimum)

#6
string = input('Введите строку: ')
print(string[0], string[3])
print(string[-1], string[-2])