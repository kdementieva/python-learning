import json
import csv

students = [
  {
    "имя": "Анна",
    "возраст": 20,
    "город": "Москва",
    "предметы": ["Python", "JavaScript"]
  },
  {
    "имя": "Петр",
    "возраст": 22,
    "город": "Санкт-Петербург",
    "предметы": ["Python", "Java"]
  },
  {
    "имя": "Мария",
    "возраст": 21,
    "город": "Киев",
    "предметы": ["JavaScript", "SQL"]
  }
]

with open('students.json', 'w', encoding='utf-8') as file:
  json.dump(students, file)

sales = [
  ['Дата', 'Продукт', 'Сумма'],
  ['2023-01-01', 'Продукт A', '500'],
  ['2023-02-15', 'Продукт B', '700'],
  ['2023-03-10', 'Продукт A', '800'],
  ['2023-04-05', 'Продукт C', '600'],
  ['2023-04-20', 'Продукт B', '900'],
  ['2023-05-12', 'Продукт A', '1000']
]

with open('sales.csv', 'w', encoding='utf-8', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows(sales) 

employees = [
  {
    "id": 1,
    "имя": "Иван",
    "должность": "Менеджер"
  },
  {
    "id": 2,
    "имя": "Елена",
    "должность": "Аналитик"
  },
  {
    "id": 3,
    "имя": "Дмитрий",
    "должность": "Разработчик"
  }
]

with open('employees.json', 'w', encoding='utf-8') as file:
  json.dump(employees, file)

performance = [
  ['employee_id', 'performance'],
  ['1', '85'],
  ['2', '92'],
  ['3', '78']
]

with open('performance.csv', 'w', encoding='utf-8') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows(performance) 



#1
def get_data():
  with open('students.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    return data

def students_quant(data):
  return len(data)

def the_oldest(data):
  oldest_student = data[0]
  max_age = int(data[0]['возраст'])
  for student in data:
    student_age = int(student['возраст'])
    if student_age > max_age:
      max_age = student_age
      oldest_student = student
  return (
    f"Имя: {oldest_student['имя']}\n"
    f"Возраст: {oldest_student['возраст']}\n"
    f"Город: {oldest_student['город']}\n"
    f"Предметы: {', '.join(oldest_student['предметы'])}"
  )

def course_students(data, course_name):
  students_on_course = []
  for student in data:
    if course_name in student['предметы']:
      students_on_course.append(student)
  print(f'Студенты на курсе {course_name}: ')
  for student in students_on_course:
    print(f'{student['имя']}, возраст: {student['возраст']}, город: {student['город']}')
  
    

students_data = get_data()
print(students_data)
print(f'Количество студентов: {students_quant(students_data)}')
print('Самый старший студент: ')
print(the_oldest(students_data))
course_students(students_data, course_name='Python')

#2
def get_data():
  data = []
  with open('sales.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
      data.append(row)
  return data

def get_sum(data):
  sale_sum = sum(int(sales['Сумма']) for sales in data)
  return sale_sum

def best_selling_product(data):
  summ_list = {}
  for product in data:
    product_name = product['Продукт']
    product_sales = int(product['Сумма'])
    if product_name in summ_list:
      summ_list[product_name] += product_sales
    else:
      summ_list[product_name] = product_sales
  best_product = max(summ_list, key=summ_list.get)
  return best_product

def month_sales(data):
  month_summ = {}
  for product in data:
    product_date = product['Дата'][:7]
    product_sales = int(product['Сумма'])
    if product_date in month_summ:
      month_summ[product_date] += product_sales
    else:
      month_summ[product_date] = product_sales
  sorted_month = sorted(month_summ.keys())
  for month in sorted_month:
    print(f'Сумма продаж за {month}: {month_summ[month]}')
  

sales_data = get_data()
print(sales_data)
print(f'Сумма продаж: {get_sum(sales_data)}')
print(f'Продукт с самым высоким объемом продаж: {best_selling_product(sales_data)}')
month_sales(sales_data)

#3
def get_data():

  with open('employees.json', 'r', encoding='utf-8') as file:
    data_json = json.load(file)

  data_csv = []
  with open('performance.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
      data_csv.append(row)

  for employee in data_json:
    for performance in data_csv:
      if employee['id'] == int(performance['employee_id']):
        employee['производительность'] = performance['performance']

  return data_json

def avg_performance(data):
  avg_perf = sum(int(performance['производительность']) for performance in data)/len(data)
  return avg_perf

def best_employee(data):
  best_employee = data[0]
  max_performance = int(data[0]['производительность'])

  for employee in data:
    emp_performance = int(employee['производительность'])
    if emp_performance > max_performance:
      max_performance = emp_performance
      best_employee = employee
  return (
    f"Имя: {best_employee['имя']}\n"
    f"Производительность: {best_employee['производительность']} "
  )

data = get_data()
print(data)
print(avg_performance(data))
print('Cотрудник с наивысшей производительностью:')
print(best_employee(data))