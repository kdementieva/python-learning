#1
s = ['apple', 'kiwi', 'banana', 'fig']
s_long = list(filter(lambda x : len(x) > 4, s))
print(s_long)

#2
students = [
    {'name' : 'John', 'grade' : 90},
    {'name' : 'Jane', 'grade' : 85},
    {'name' : 'Dave', 'grade' : 92}
]

max_grade = max(students, key=lambda student : student['grade'])
print(max_grade)

#3
t = [(1, 5), (3, 2), (2, 8), (4, 3)]
sorted_t = sorted(t, key=lambda x: x[0] + x[1])
print(sorted_t)

#4
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)

#5
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name = '{self.name}', age ='{self.age}')"
    

persons = [
    Person('Anna', 25),
    Person('Adrian', 48),
    Person('Agnieszka', 47),
    Person('Piotr', 16)
]

sort_age = sorted(persons, key=lambda x: x.age)
print(sort_age)