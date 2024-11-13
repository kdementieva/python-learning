class Course:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def get_absolute_url(self):
        return f'https://ivashev-edu.com/courses/{self.title.replace(' ', '-')}'


class StudentProfile:
    def __init__(self, full_name, email):
        self.full_name = full_name
        self.email = email

    def get_absolute_url(self):
        return f'https://ivashev-edu.com/profiles/{self.full_name.lower().replace(' ', '')}'
    

class1 = Course('Python Basics', 5)
class2 = Course("Data Science", 12)
student1 = StudentProfile('John Doe', 'john117@gmail.com')
student2 = StudentProfile("Jane Smith", "jane.smith@example.com")

print(class1.get_absolute_url())
print(class2.get_absolute_url())
print(student1.get_absolute_url())
print(student2.get_absolute_url())