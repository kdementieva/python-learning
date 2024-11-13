#1
class Publication:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return (
            f'Название публикации: {self.title}\n'
            f'Автор публикации: {self.author}\n'
            f'Год издания публикации: {self.year} \n'
        )


class Book(Publication):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre

    def get_info(self):
        result = super().get_info()
        return f'''{result}Жанр публикации: {self.genre} \n'''


class Magazine(Publication):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def get_info(self):
        result = super().get_info()
        return f'''{result}Номер выпуска публикации: {self.issue_number} \n'''

class Newspaper(Publication):
    def __init__(self, title, author, year, publisher):
        super().__init__(title, author, year)
        self.publisher = publisher

    def get_info(self):
        result = super().get_info()
        return f'''{result}Издатель публикации: {self.publisher} \n'''
    


book1 = Book("Harry Potter", "J.K. Rowling", 1997, "Fantasy")
book2 = Book("1984", "George Orwell", 1949, "Dystopian")
magazine1 = Magazine("National Geographic", "Various Authors", 2024, "102")
magazine2 = Magazine("Time", "Various Authors", 2024, "101")
newspaper1 = Newspaper("The Times", "John Doe", 2024, "The Times Publishing")
newspaper2 = Newspaper("The Guardian", "Jane Roe", 2024, "Guardian News & Media")

print(book1.get_info())
print(book2.get_info())
print(magazine1.get_info())
print(magazine2.get_info())
print(newspaper1.get_info())
print(magazine2.get_info())


#2
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f'''Название продукта: {self.name} 
Цена продукта: {self.price}'''

class Product(Item):
    def __init__(self, name, price, brand, category):
        super().__init__(name, price)
        self.brand = brand
        self.category = category

    def get_brand(self):
        return f'''Бренд продукта: {self.brand}'''
    
class Food(Product):
    def __init__(self, name, price, brand, category, expiry_date, weight):
        super().__init__(name, price, brand, category)
        self.expiry_date = expiry_date
        self.weight = weight

    def get_expiry_date(self):
        return f'''Срок годности продукта: {self.expiry_date}'''

class Beverage(Product):
    def __init__(self, name, price, brand, category, volume, carbonated):
        super().__init__(name, price, brand, category)
        self.volume = volume
        self.carbonated = carbonated
    
    def is_carbonated(self):
        return f'''Является ли газированным: {self.carbonated}'''

food1 = Food("Banana", 1.99, "Chiquita", "Fruit", "2023-01-31", 150)
food2 = Food("Cheese", 4.99, "Kraft", "Dairy", "2022-12-15", 250)

beverage1 = Beverage("Coca Cola", 2.49, "Coca Cola Company", "Soft Drink", 500, True)
beverage2 = Beverage("Water", 0.99, "Aquafina", "Bottled Water", 1000, False)

print(food1.get_info())
print(food1.get_brand())
print(food1.get_expiry_date())

print(beverage2.get_info())
print(beverage2.get_brand())
print(beverage2.is_carbonated())