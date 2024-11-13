class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address.city}, {self.address.street}")


my_address = Address("New York", "Broadway")
my_person = Person("John Doe", my_address)
my_person.display_info()