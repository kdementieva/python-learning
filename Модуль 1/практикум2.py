account1 = {'login' : 'ivan', 'password' : 'q1'}
account2 = {'login' : 'petr', 'password' : 'q2'}
account3 = {'login' : 'olga', 'password' : 'q3'}
account4 = {'login' : 'anna', 'password' : 'q4'}

user1 = {'name' : 'Иван', 'age' : '20', 'account' : account1}
user2 = {'name' : 'Петр', 'age' : '25', 'account' : account2}
user3 = {'name' : 'Ольга', 'age' : '18', 'account' : account3}
user4 = {'name' : 'Анна', 'age' : '27', 'account' : account4}

user_list = [user1,user2,user3,user4]

#1
log = input('Введите ключ (name или account): ')
log_ = log.lower()
if log_ in user1:
    print(f'значение ключа {log_} для юзера 1 = {user1[log_]}')
    print(f'значение ключа {log_} для юзера 1 = {user2[log_]}')
    print(f'значение ключа {log_} для юзера 1 = {user3[log_]}')
    print(f'значение ключа {log_} для юзера 1 = {user4[log_]}')
else:
    print('Введенный ключ не найден')

#2
num = int(input('Введите порядковый номер: '))
if 1 <= num <= len(user_list):
    user = user_list[num - 1]
    print(f'''Данные по юзеру № {num}:
имя: {user['name']}
возраст: {user['age']}
логин: {user['account']['login']}
пароль: {user['account']['password']} ''')
else:
    print('Пользователь с указанным номером не найден')

#3
ask = int(input('Введите номер пользователя, которого нужно переместить в конец: '))

print('До изменения: ', user_list)
index = user_list.pop(ask - 1)
user_list.append(index)
print('Перемещенный пользователь: ', index)
print('После изменения: ', user_list)

#4
ages = list(map(int, [user['age'] for user in user_list])) #выношу возраста в отдельный список
average = sum(ages)/len(ages)
print(f'Средний возраст всех юзеров: {average}')