import csv

#Задание 0

# with open(r'test.csv', encoding='utf-8') as csvfile:
#   reader = csv.reader(csvfile)
#   for row in reader:
#     print(row)  # Выводим каждую строку файла
#     print(list(reader))

# data = [
#     ['Имя', 'Возраст', 'Город'],
#     ['Анна', '25', 'Москва'],
#     ['Петр', '30', 'Санкт-Петербург'],
#     ['Мария', '28', 'Киев']
# ]

# # Открываем файл для записи
# with open('новые_данные.csv', 'w', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(data)  # Записываем данные в файл

# data = [
#     {'Имя': 'Анна', 'Возраст': '25', 'Город': 'Москва'},
#     {'Имя': 'Петр', 'Возраст': '30', 'Город': 'Санкт-Петербург'},
#     {'Имя': 'Мария', 'Возраст': '28', 'Город': 'Киев'}
# ]

# # Записываем данные в CSV файл с использованием словаря
# with open('данные_с_заголовками.csv', 'w', encoding='utf-8') as csvfile:
#     fieldnames = ['Имя', 'Возраст', 'Город']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#     writer.writeheader()  # Записываем заголовки
#     writer.writerows(data)  # Записываем данные

# # Чтение данных из CSV файла с использованием словаря
# with open('данные_с_заголовками.csv', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['Имя'], row['Возраст'], row['Город'])

#Задание 1

def get_data():
  data = []
  with open('prices.txt', encoding='utf-8') as f:
    for line in f:
      text = line.rstrip().split('\t')
      data.append(text)
  return data

def new_csv():
  headers = ['Наименование товара', 'Количество товара', 'Цена/шт']

  with open('prices.csv', 'w', encoding='utf-8', newline='') as csvfile: #newline, чтобы не добавлял пустых строк
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(get_data())

#Задание 2

def find_sum():
  total_price = 0
  with open('prices.csv', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
      quant = int(row['Количество товара'])
      price_per_unit = int(row['Цена/шт'])
      total_price += quant * price_per_unit
  return total_price
      

print(find_sum())