# a = 15.8
# print(a, type(a))

# val = int(input())
# print(val, type(val))
# print(val*5)

# val = input('Введите какое-то значение: ')
# print(val)
# print(type(val))

# name = 'Irina'
# city = 'Msk'
# age = 30

# info = f'My name is {name}, I am from {city}, I am {age} old '
# print(info)

# stroka = 'Hello, world!'
# print(dir(stroka))
# print(stroka.upper())
# print(stroka.lower())
# print(stroka.replace('Hello', 'Bye').replace('world', 'friend'))
# print(stroka.find(','))
# print(stroka.find('o'))
# print(stroka.rfind('o'))

# numbers = {
#     '1': 'one',
#     '2': 'two',
#     '3': 'three',
#     '4': 'four',
#     '5': 'five',
#     '6': 'six',
#     '7': 'seven',
#     '8': 'eight',
#     '9': 'nine',
#     '0': 'zero'
# }

# my_number = input('Input a number: ')
# number = 0

# try:
#     number = int(my_number)
#     result = []

#     for digit in list(my_number):
#         result.append(numbers[digit])

#     print(' '.join(result))
# except:
#     print('This is not a number.')



# temp = float(input())

# if temp > 37:
#     print('Остаемся дома')
# else:
#     print('Идем на работу')

# a = int(input())
# if a % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# text = "Привет, мир!" 
# if "мир" in text: 
#     print("Строка содержит слово 'мир'.")



# fruits = ['apple', 'banana', 'kiwi', 'mango', 'orange']

# for i in fruits:
#     print(i)
    
# str = 'Qwerty 123'

# for i in str:
#     print(i)


# numbers = [1, 2, 3, 4, 5] 
# summ = 0 
# for number in numbers: 
#     summ += number
# print("Сумма чисел: ", summ)

# message = "Hello, world!" 
# for char in message: 
#     print(char)


# numbers = [1, 2, 3, 4, 5] 
# for num in numbers: 
#     if num % 2 == 0: 
#         print(num)
    

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
# for row in matrix: 
#     for num in row: 
#         print(num)
    

# my_dict = {'a': 1, 'b': 2, 'c': 3} 
# for key in my_dict: 
#     print(key)

# # или аналогичный вариант
# for key in my_dict.keys(): 
#     print(key)

# my_dict = {'a': 1, 'b': 2, 'c': 3} 
# for value in my_dict.values(): 
#     print(value)

# my_dict = {'a': 1, 'b': 2, 'c': 3} 
# for key, value in my_dict.items(): 
#     print(key, value)

# i = 1 
# while i <= 5: 
#     print(i) 
#     i += 1

# password = ""
# while password != "secret":
#     password = input("Введите пароль: ")
# print("Доступ разрешен!")


# n = 10
# fib = [0, 1]
# while len(fib) < n:
#     fib.append(fib[-1] + fib[-2])
# print(fib)


# n = 5
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print(fact)


# for i in range(10):
#     if i == 5:
#         break
#     print(i)


# while True:
#     answer = input("Какой ваш любимый цвет? ")
#     if answer.lower() == "синий":
#         print("Мой тоже!")
#         break
#     else:
#         print("О, это интересный выбор.")

    
# fruits = ['apple', 'banana', 'kiwi', 'mango', 'orange']
# search = 'kiwi'
# i = 0
# while i < len(fruits):
#     if fruits[i] == search:
#         print(search, "найден!")
#         break
#     i += 1
# else:
#     print(search, "не найден.")

# fruits = ['apple', 'banana', 'kiwi', 'mango', 'orange']
# search = 'kiwi'
# for i in range(len(fruits)):
#     if search == fruits[i]:
#         print(search, "найден!")


# for i in range(10):
#     if i == 5:
#         print('_______________')
#         continue
#     print(i)

# cars = int(input('Введите количество машин: '))
# if 1 <= cars <= 30:
#     speed = 0
#     count = 0
#     fast_car = 0
#     smallest = None
#     while count <= cars - 1:
#         speed = float(input('Введите cкорость: '))
#         if 1 <= speed <= 300:
#             speed_rnd = round(speed)
#             if speed_rnd > 80:
#                 fast_car += 1
#             if smallest is None or speed_rnd < smallest:
#                 smallest = speed_rnd
#         else:
#             print('Неправильное значение!')
#             continue
#         count += 1
#     if fast_car > 0:
#         print(smallest, 'YES')
#     else:
#         print(smallest, 'NO')
# else:
#     print('Неправильное значение!')

# cars_amount = int(input('Input cars amount: '))

# if 1 > cars_amount > 30:
#     print('Cars amount has to be between 1 and 30')
#     exit()

# car_index = 0
# any_car_exceeded_limit = 'NO'
# smallest_speed = 301

# while car_index < cars_amount:
#     car_speed = round(float(input('Input car speed: ')))

#     if 1 > car_speed > 300:
#         print('Car speed has to be between 1 and 300')
#         continue

#     if car_speed > 80 and any_car_exceeded_limit == 'NO':
#         any_car_exceeded_limit = 'YES'

#     if smallest_speed > car_speed:
#         smallest_speed = car_speed
    
#     car_index += 1

# print(f'{smallest_speed} {any_car_exceeded_limit}')


# def countdown(n):
#     if n <= 0:
#         print("Done!")
#     else:
#         print(n)
#         countdown(n - 1)

# countdown(5)  # выводит числа от 5 до 1 и "Done!"

# def get_name_length(name):
#     length = len(name)
#     first_letter = name[0]
#     last_letter = name[-1]
#     return length, first_letter, last_letter

# result = get_name_length("Alice")
# print(result)  # выводит (5, 'A', 'e')

# def greet(name="Guest"):
#     print("Hello, " + name + "!")

# greet()  # выводит "Hello, Guest!"
# greet("Alice")  # выводит "Hello, Alice!"

# def my_function(*args):
#     print(args) # тут уже будет кортеж из всех переданных элементов
#     for arg in args:
#         print(arg)

# my_function(1, 2, 3, 4)

# def my_function(a, b, c):
#     print(a, b, c)

# my_tuple = (1, 2, 3)
# my_function(*my_tuple)

# def greet(name, age):
#     print(f"Привет, {name}! Тебе {age} лет.")

# user_info = {"name": "Алиса", "age": 30}
# greet(**user_info)

# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name="John", age=25, city="New York")


# try:
#     # Код, который может вызвать исключение
#     result = 10 / 0
# except ZeroDivisionError:
#     # Код обработки исключения
#     print("Деление на ноль не допускается!")

# try:
#     # Код, который может вызвать исключение
#     result = 10 / 2
# except ZeroDivisionError:
#     # Код обработки исключения
#     print("Деление на ноль не допускается!")
# else:
#     # Код, выполняющийся, если исключение не возникло
#     print("Результат:", result)

# try:
#     # Код, который может вызвать исключение
#     result = 10 / 2
# except ZeroDivisionError:
#     # Код обработки исключения
#     print("Деление на ноль не допускается!")
# finally:
#     # Код, выполняющийся всегда
#     print("Конец программы")

#________________________________________________________________________________________________
#Обработка конкретного исключения:
# try:
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число: "))
#     result = num1 / num2
#     print("Результат деления:", result)
# except ZeroDivisionError:
#     print("Деление на ноль не допускается!")
# except ValueError:
#     print("Ошибка ввода числа!")


#Обработка нескольких исключений одновременно:
# try:
#     num = int(input("Введите число: "))
#     result = 10 / num
#     print("Результат:", result)
# except (ZeroDivisionError, ValueError):
#     print("Ошибка ввода числа или деление на ноль!")


#Использование общего исключения для перехвата всех ошибок:
# try:
#     num = int(input("Введите число: "))
#     result = 10 / num
# except Exception as e:
#     print("Произошла ошибка:", str(e))



# numbers = [1, 2, 3, 4, 5] 
# squared_numbers = [] 

# for num in numbers: 
#     squared_numbers.append(num**2) 

# print(squared_numbers)  # Вывод: [1, 4, 9, 16, 25]

# numbers = [1, 2, 3, 4, 5] 
# squared_numbers = [num**2 for num in numbers]
# print(squared_numbers)  # Вывод: [1, 4, 9, 16, 25]

# numbers = {x: x**2 for x in range(1, 6)}
# print(numbers)  # Вывод: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# numbers = [1, 2, 3, 4, 5] 
# even_odd = {num: 'even' if num % 2 == 0 else 'odd' for num in numbers} 
# print(even_odd)  # Вывод: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

# import requests

# # Отправка GET-запроса на сайт 'https://google.com'
# response = requests.get('https://google.com')

# # Проверка статус-кода ответа
# if response.status_code == 200:
#     print('Запрос выполнен успешно')
# else:
#     print('Произошла ошибка:', response.status_code)

# # Вывод содержимого ответа
# # print(response.text)
# # print(response.headers)
# content_type = response.headers['Content-Type']
# print(content_type)

# -------------------------------------------------------------------------------------
# class Stack:
#     def __init__(self):
#         self.items = []

#     def is_empty(self):
#         return len(self.items) == 0

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             raise IndexError("Стек пуст")

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#         else:
#             raise IndexError("Стек пуст")

#     def size(self):
#         return len(self.items)

# # Создаем экземпляр стека
# my_stack = Stack()

# # Добавляем элементы в стек
# my_stack.push(5)
# my_stack.push(10)
# my_stack.push(15)

# # Просматриваем вершину стека
# print("Вершина стека:", my_stack.peek())

# # Удаляем элемент из стека
# my_stack.pop()

# # Проверяем, пуст ли стек
# print("Стек пуст?", my_stack.is_empty())

# # Выводим размер стека
# print("Размер стека:", my_stack.size())


# ---------------------------------------------------------------------------------------------------------------------------------
#BFS
# from collections import deque

# def bfs(graph, start):
#     visited = set()  # Множество для отслеживания посещенных вершин
#     queue = deque()   # Очередь для обхода

#     queue.append(start)
#     visited.add(start)

#     while queue:
#         vertex = queue.popleft()
#         print(vertex)  # Посещаем вершину (выполняем необходимые действия)

#         for neighbor in graph[vertex]:
#             if neighbor not in visited:
#                 queue.append(neighbor)
#                 visited.add(neighbor)

# # Пример использования:

# graph = {
#     0: [1,2,3],
#     1: [0,2],
#     2: [0,1,4],
#     3: [0],
#     4: [2]
# }

# bfs(graph, 0)

# -----------------------------------------------------------------------------------------------------
# Merge sort

# def merge_sort(arr):
#     # Шаг 1: Проверяем, если длина массива больше 1, то продолжаем сортировку
#     if len(arr) > 1:
#         middle = len(arr) // 2  # Находим средний индекс массива
#         left_half = arr[:middle]  # Делим массив на две половины: левую и правую
#         right_half = arr[middle:]

#         # Шаг 2: Рекурсивно сортируем обе половины
#         merge_sort(left_half)
#         merge_sort(right_half)

#         # Шаг 3: Слияние (merge) отсортированных половин
#         i = j = k = 0  # Индексы для левой, правой и общей частей массива

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1

#         # Если в одной из половин остались элементы, добавляем их в конец
#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1

# # Пример использования:
# my_list = [64, 34, 25, 12, 22, 11, 90]
# merge_sort(my_list)
# print("Отсортированный список:", my_list)

# -----------------------------------------------------------------------------------------------------
# Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Если массив пустой или содержит один элемент, он считается отсортированным

    pivot = arr[len(arr) // 2]  # Выбираем опорный элемент (в данном случае, средний элемент)
    left = [x for x in arr if x < pivot]  # Элементы меньше опорного
    middle = [x for x in arr if x == pivot]  # Элементы равные опорному
    right = [x for x in arr if x > pivot]  # Элементы больше опорного

    # Рекурсивно сортируем левую и правую части, а затем объединяем их с опорным элементом
    return quick_sort(left) + middle + quick_sort(right)

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = quick_sort(my_list)
print("Отсортированный список:", sorted_list)