class Engine():
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
    
    def __str__(self):
        return (
            f'Максимальная мощность: {self.horsepower} (в лошадиных силах) \n'
            f'Тип топлива: {self.fuel_type}'
            )
    
class CarBody():
    def __init__(self, body_type, door_number):
        self.body_type = body_type
        self.door_number = door_number

    def __str__(self):
        return (
            f'Тип кузова: {self.body_type} \n'
            f'Количество дверей: {self.door_number}'
        )

class Wheel():
    def __init__(self, diameter, tire_type):
        self.diameter = diameter
        self.tire_type = tire_type

    def __str__(self):
        return (
            f'Диаметр колеса: {self.diameter}\n'
            f'Тип резины: {self.tire_type}'
        )

class Car():
    def __init__(self, horsepower, fuel_type, body_type, door_number, diameter, tire_type):
        self.engine = Engine(horsepower, fuel_type)
        self.body = CarBody(body_type, door_number)
        self.wheels = [Wheel(diameter, tire_type) for _ in range(4)]
    
    def display_engine_info(self):
        return self.engine
    
    def display_car_body_info(self):
        return self.body
    
    def display_wheel_info(self):
        return "\n".join([f"Колесо {i+1}:\n{str(wheel)}" for i, wheel in enumerate(self.wheels)])
    #enumerate создает пары индекс объект
    
car1 = Car(120, "Бензин", "Хэтчбек", 4, 15, "Летняя")
car2 = Car(200, "Дизель", "Седан", 4, 16, "Всесезонная")
car3 = Car(150, "Электро", "Купе", 2, 17, "Зимняя")
car4 = Car(250, "Гибрид", "Внедорожник", 5, 18, "Грязевая")

print("Автомобиль 1:")
print(car1.display_engine_info())
print(car1.display_car_body_info())
print(car1.display_wheel_info())
print()
print("Автомобиль 2:")
print(car2.display_engine_info())
print(car2.display_car_body_info())
print(car2.display_wheel_info())
print()
print("Автомобиль 3:")
print(car3.display_engine_info())
print(car3.display_car_body_info())
print(car3.display_wheel_info())
print()
print("Автомобиль 4:")
print(car4.display_engine_info())
print(car4.display_car_body_info())
print(car4.display_wheel_info())
print()