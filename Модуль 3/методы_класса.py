class Rectangle:
    width = 0
    height = 0

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

rectangle1 = Rectangle()
rectangle1.height = 20
rectangle1.width = 30

rectangle1.display_info()
rectangle1.resize(10,11)
rectangle1.display_info()
