class Car:
    make = ''
    model = ''
    year = 0

    def display_info(self):
        print(f"Car: {self.make} {self.model} ({self.year})")

    def update_year(self, new_year):
        self.year = new_year

car1 = Car()
car1.make = 'BMW'
car1.model = 'X5'
car1.year = 2019

car2 = Car()
car2.make = 'Mercedes'
car2.model = 'AMG'
car2.year = 2015

car3 = Car()
car3.make = 'Audi'
car3.model = 'A4'
car3.year = 2022

print('Марка:', car1.make)
print('Модель:', car1.model)
print('Год:', car1.year)

print('Марка:', car2.make)
print('Модель:', car2.model)
print('Год:', car2.year)

print('Марка:', car3.make)
print('Модель:', car3.model)
print('Год:', car3.year)


car1.display_info()  # Вывод: Car: BMW X5 (2021)
car2.display_info() # Car: Audi A4 (2022)

car1.display_info()  # Вывод: Car: BMW X5 (2021)

car1.update_year(2022)
car1.display_info()  # Вывод: Car: BMW X5 (2022)
display_info()