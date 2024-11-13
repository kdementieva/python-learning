from dataclasses import dataclass

@dataclass
class Student:
  name: str
  age: int
  major: str
  gpa: float

  def display_info(self):
    return (
      f'Student name: {self.name}\n'
      f'Student age: {self.age}\n'
      f'Student major: {self.major}\n'
      f'Student grade: {self.gpa}\n'
    )
  def calculate_grade(self):
    if self.gpa == 5:
      return 'Excellent'
    if 4 <= self.gpa < 5:
      return 'Good'
    if 3 <= self.gpa < 4:
      return 'Satisfactory'
    if self.gpa < 3:
      return 'Unsatisfactory'
    

def sorting_students(students):
    return sorted (students, key=lambda student: student.gpa, reverse=True)

       
# Создание списка студентов
students = [
    Student("Alice", 20, "Computer Science", 3.8),
    Student("Bob", 22, "Engineering", 3.2),
    Student("Charlie", 21, "Mathematics", 4.5),
    Student("David", 23, "Physics", 2.7),
    Student("Eve", 19, "Biology", 3.9)
]

sorted_students = sorting_students(students)
print(sorted_students)

# Отображение информации о студентах
for student in students:
    	print(student.display_info())

# Сравнение студентов
print("Are Alice and Bob the same student?", students[0] == students[1])
print("Are Alice and Eve the same student?", students[0] == students[4])

# Расчет и вывод оценок
for student in students:
    print(f"{student.name} - Grade: {student.calculate_grade()}")
