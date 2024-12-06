from functools import reduce

def cube(x):
  return x ** 3

def div_by_5(x):
  return x % 5 == 0

def multiply_odd(x, y):
  if x % 2 != 0 and y % 2 != 0:
    return x * y
  return x if x % 2 != 0 else y


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
in_cube = list(map(cube, numbers))
print(in_cube)

num_div_by_5 = list(filter(div_by_5, numbers))
print(num_div_by_5)

product = reduce(multiply_odd, numbers)
print(product)