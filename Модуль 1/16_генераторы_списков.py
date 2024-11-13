#1
squared_numbers = [x**2 for x in range(1, 11)]
print(squared_numbers)

#2
even = [x for x in range(1, 21) if x % 2 == 0]
print(even)

#3
squared_numbers = [x**2 for x in range(1, 11) if x > 5]
print(squared_numbers)

#4
word = 'Hello'
letters = [char.upper() for char in word]
print(letters)

#5
words = ['apple', 'banana', 'cherry', 'orange']
words_length = [word for word in words if len(word) > 5]
print(words_length)