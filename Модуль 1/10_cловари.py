#0
my_dict = {'apple': 1, 'banana': 2, 'orange': 3}  
my_dict['grape'] = 4
del my_dict['banana']
print('apple' in my_dict)
my_dict.clear() 
print(my_dict)
my_dict = {'apple': 2, 'banana': 3, 'orange': 4} 
new_dict = my_dict.copy()
print(new_dict) 
print(my_dict.get('apple'))
print(my_dict.get('pear', 0))
print(my_dict.items()) 
print(my_dict.keys())
print(my_dict.values())
print(my_dict.pop('apple'))
print(my_dict.pop('pear', 0))
print(my_dict)
print(my_dict.popitem())
print(my_dict)
my_dict = {'apple': 2, 'banana': 3, 'orange': 4} 
new_dict = {'pear': 5, 'kiwi': 6} 
my_dict.update(new_dict) 
print(my_dict) 

#1
info = {'name' : 'Kateryna', 'age' : 23, 'color' : 'purple'}
print(info)

#2
movies = {
    'Inception': ['Leonardo DiCaprio', 'Joseph Gordon-Levitt', 'Elliot Page'],
    'The Matrix': ['Keanu Reeves', 'Laurence Fishburne', 'Carrie-Anne Moss'],
    'Interstellar': ['Matthew McConaughey', 'Anne Hathaway', 'Jessica Chastain'],
    'The Dark Knight': ['Christian Bale', 'Heath Ledger', 'Gary Oldman']
}

name = input('Введите название фильма: ')
bd = movies.get(name, 'Фильм не найден')
print(bd)

#3
countries = {
    'Ukraine': {'capital': 'Kyiv', 'population': 41_167_336},
    'Poland': {'capital': 'Warsaw', 'population': 38_179_800},
    'Germany': {'capital': 'Berlin', 'population': 83_240_525},
    'France': {'capital': 'Paris', 'population': 67_848_156}
}

print(countries)

#4
games = {
    'The Witcher 3: Wild Hunt': {'genre': 'Action RPG', 'release_year': 2015},
    'Cyberpunk 2077': {'genre': 'Action RPG', 'release_year': 2020},
    'Minecraft': {'genre': 'Sandbox', 'release_year': 2011},
    'The Last of Us Part II': {'genre': 'Action-adventure', 'release_year': 2020},
    'Elden Ring': {'genre': 'Action RPG', 'release_year': 2022}
}

for game, info in games.items(): #цикл for перебирает каждый кортеж(game.items()) для ключа game
    print(f'Игра: {game}')
    print(f'Жанр: {info['genre']}')
    print(f'Год выпуска: {info['release_year']}')
    print() # не знаю в каком виде надо было вывести список

#5
countries = {
    'Ukraine': 'Kyiv',
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'France': 'Paris',
    'Japan': 'Tokyo',
    'Canada': 'Ottawa',
    'Brazil': 'Brasília',
    'Australia': 'Canberra',
    'Egypt': 'Cairo'
}

print(countries)

#6
fruits = {
    'Яблоко': 250,  
    'Банан': 60,
    'Апельсин': 90,
    'Виноград': 300,
    'Ананас': 200,
    'Клубника': 500,
    'Манго': 150,
    'Киви': 400
}

name = input('Введите название фруктов: ')
kg = input('Введите вес фруктов: ')
kg_float = float(kg)
price = fruits[name]
check = price * kg_float
print(check)

