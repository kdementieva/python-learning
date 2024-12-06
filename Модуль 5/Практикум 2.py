from collections import namedtuple, Counter, deque, defaultdict
import random

#1
rand_list = []
for i in range(10):
  rand_list.append(random.randint(1, 11))
print(rand_list)

counter = Counter(rand_list)
counter_sort = dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))
most_common = list(counter_sort.items())[:3]
print(counter_sort)
print(most_common)

#2
Book = namedtuple('Book', ['title', 'author', 'genre'])

book1 = Book(title="1984", author="George Orwell", genre="Dystopian")
book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", genre="Classic")
book3 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Novel")
book4 = Book(title="Moby Dick", author="Herman Melville", genre="Adventure")

print(
  f'Название книги: {book1.title}\n'
  f'Автор: {book1.author}\n'
  f'Жанр: {book1.genre}'    
  )

#3
dictionary = defaultdict(list)
dictionary['fruits'].extend(['apple','banana'])
dictionary['vegetables'].extend(['carrot'])
dictionary['drinks'].extend(['water', 'juice', 'soda'])

for key, value in dictionary.items():
  print(f'{key}: {value}')

#4
queue = deque([3, 9, 9, 7, 5, 6, 3, 9, 2, 5])
queue.append(4)
print(queue)
queue.appendleft(2)
print(queue)
queue.pop()
print(queue)
queue.popleft()
print(queue)

#5
def add_to_deque(dq, el, to_front=False):
  if to_front:
    dq.appendleft(el)
  else:
    dq.append(el)

def remove_from_deque(dq, from_front=True):
  if from_front:
    dq.popleft() 
  else:
    dq.pop()
  
new_queue = deque([3, 9, 1, 7, 7, 6, 10, 6, 8, 9])
add_to_deque(new_queue, 10)
add_to_deque(new_queue, 22, True)
print(new_queue)
remove_from_deque(new_queue)
remove_from_deque(new_queue, False)
print(new_queue)