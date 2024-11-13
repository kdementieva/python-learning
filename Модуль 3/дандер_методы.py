class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        area = self.width * self.height
        return area
    
    def resize(self, width, height):
        self.width = width
        self.height = height
    
    def display_info(self):
        area = self.calculate_area()
        print(f'Высота прямоугольника = {self.height}')
        print(f'Ширина прямоугольника = {self.width}')
        print(f'Площадь прямоугольника = {area}')
        
    def __str__(self):
        return f'Прямоугольник: ширина = {self.width}, высота = {self.height}'

rectangle1 = Rectangle(20, 30)
rectangle2 = Rectangle(30, 70)
rectangle3 = Rectangle(20, 40)

print(rectangle1)
print(rectangle2)
print(rectangle3)
