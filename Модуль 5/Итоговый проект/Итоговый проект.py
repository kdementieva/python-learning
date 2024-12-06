import json
import csv

def get_data():
  with open('student_list.json', 'r', encoding='utf-8') as file:
    return json.load(file)
    
def get_average_score(students):
  average_scores = {
    student: sum(info['grades'].values()) / len(info['grades']) 
    for student, info in students.items()
    }
  for student, average_score in average_scores.items():
    print(f'Средний балл для студента {student}: {average_score}')
  return average_scores

def get_best_student(avg_scores):
  max_grade = max(avg_scores.items(), key=lambda x: x[1])
  return max_grade

def get_worst_student(avg_scores):
  min_grade = min(avg_scores.items(), key=lambda x: x[1])
  return min_grade

def find_student(students, name):
  if name in students:
    student_info = students[name]
    return (
      f'Имя: {name}\n'
      f'Возраст: {student_info['age']}\n'
      f'Предметы: {student_info['subjects']}\n'
      f'Оценки: {student_info['grades']}\n'
    )
  else:
    return 'Студент с таким именем не найден'

def sort_by_grades(avg_scores):
  sorted_grades = sorted(avg_scores.items(), key=lambda x: x[1], reverse=True)
  print('Сортировка студентов по среднему баллу:\n')
  for student in sorted_grades:
    print(f'{student[0]}: {student[1]}')

def dict_to_list(students):
  new_students = []
  for name, info in students.items():
    new_students.append({
      'name' : name,
      'age' : info['age'],
      'subjects' : info['subjects'],
      'grades' : info['grades']
    })
  return new_students

def data_to_csv(avg_scores, students):
  student_list = []
  for name, info in students.items():
    student_list.append({
      'name' : name,
      'age' : info['age'],
      'grade' : avg_scores[name]
    })
    
  with open('student_list.csv', 'w', encoding='utf-8', newline='') as file:
    fieldnames = ['name', 'age', 'grade']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(student_list)

students = get_data()
average_scores = get_average_score(students)
print(f'Наилучший студент: {get_best_student(average_scores)[0]} (Средний балл: {get_best_student(average_scores)[1]})')
print(f'Худший студент: {get_worst_student(average_scores)[0]} (Средний балл: {get_worst_student(average_scores)[1]})')
print(find_student(students, input('Введите имя студента: ').capitalize()))
sort_by_grades(average_scores)
print(dict_to_list(students))
data_to_csv(average_scores, students)