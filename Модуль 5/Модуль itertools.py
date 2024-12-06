import itertools

#1
items = [1, 2, 3, 4]
for c in itertools.combinations(items, 2):
    print(c)

#2
s = 'Python'
for p in itertools.permutations(s):
    print(p)

#3
list_1 = ['a', 'b']
list_2 = [1, 2, 3]
list_3 = ['x', 'y']

chained = itertools.chain(list_1, list_2, list_3)
count = 0
for i in itertools.cycle(chained):
    if count > 6:
        break
    print(i)
    count += 1

#4
def fibonacci():
    a, b = 0, 1
    while True:
        yield a # генератор, который возвращает по одному значению за раз
        a, b = b, a + b

fib = fibonacci()
for i in itertools.islice(fib, 11):
    print(i)
    
#5
list1 = ['red', 'blue']
list2 = ['shirt', 'shoes']
for i in itertools.product(list1, list2):
    print(i)

