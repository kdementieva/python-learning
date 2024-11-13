#1
primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71) 
print(primes[:6])

#2
data = 'Python для продвинутых!'
t_data = tuple(data)
print(t_data)

#3
numbers = {1.414, 12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324, 2.718, 1.324}
min_ = min(numbers)
max_ = max(numbers)
sum_ = min_ + max_
print(sum_)

#4
s = 4, 5, 76, 78, 89, 92, 2
z = 6.8, 8, 3, 6, 9, 9, 4, 3
s = set(s)
z = set(z)
# check = s - z
# print(check)
check = s.isdisjoint(z)
print(check)


#5
s = 'Snowflakes, snowflakes falling down. Snowflakes, covering up the ground. Making a blanket, soft and white. Making a blanket in the night.'
s = s.lower().replace(',', ' ').replace('.', ' ')
s = s.split()
s = set(s)
l = len(s)
print(l)

#6
sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) 
when I was three, and, save for a pocket of warmth in the darkest past, nothing of her 
subsists within the hollows and dells of memory, over which, if you can still stand my style 
(I am writing under observation), the sun of my infancy had set: surely, you all know those redolent 
remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and 
traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
s = sentence.lower().replace(',', ' ').replace('.', ' ').replace(')', ' ').replace('(', ' ').replace(';', ' ').replace(':', ' ')
s = s.split()
s = set(s)
s = sorted(s)
print(' '.join(s))

#7
num = input('Введите целое натуральное число: ')

new_num = num.replace('0', 'zero ').replace('1', 'one ').replace('2', 'two ').replace('3', 'three ').replace('4', 'four ').replace('5', 'five ').replace('6', 'six ').replace('7', 'seven ').replace('8', 'eight ').replace('9', 'nine ')
print(new_num)
# number_to_words = {'0': 'zero', 
#                    '1': 'one', 
#                    '2': 'two', 
#                    '3': 'three', 
#                    '4': 'four', 
#                    '5': 'five', 
#                    '6': 'six', 
#                    '7': 'seven', 
#                    '8': 'eight', 
#                    '9': 'nine'}
# num = input('Введите целое натуральное число: ')
# print(' '.join([number_to_words[number] for number in num])) 
#Hемножко залезла в интернет для решения этой задачи.
# Hасколько я понимаю, с помощью слова-ключ(в этом случае number, 
# которое сравнивается со строкой num) он ищет подходящее значение
# в словаре, который я сама определила. А слово for проходит по каждому элементу в num.

