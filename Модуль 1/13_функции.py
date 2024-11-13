#1
def calculate_average(a):
    return sum(a) / len(a)

print(calculate_average([23, 732, 63, 84, 898, 21]))

#2
def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False
    
print(is_even(7))

#3
def count_vowels(s):
    s = s.lower()
    quant = 0
    for i in range(len(s)):
        if s[i] in 'aeouy':
            quant += 1
    return quant

print(count_vowels('Even though theyre only a few letters'))

#4
def find_max(l):
    return max(l)

print(find_max([23, 45, 2738, 3, 0]))

#5
def reverse_string(s):
    return s[::-1]

print(reverse_string('Шла Саша по шоссе'))

#6
def is_palindrome(s):
    s = s.lower()
    symbols_to_remove = ',!?. '
    for symbol in symbols_to_remove:
        s = s.replace(symbol, '')
    s_end = s[::-1]
    if s == s_end:
        return True
    else:
        return False
    
print(is_palindrome('Jeż leje lwa, paw leje lżej'))

#7
def calculate_factorial(a):
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result

print(calculate_factorial(5))

#8
def is_prime(a):
    if a < 2: 
        return False
    for d in range(2, int(a ** 0.5) + 1):
        if a % d == 0:
            return False
    return True

print(is_prime(67))

#9
def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return[0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci_result = [0, 1]
        for i in range(2, n):
            fib_sum = fibonacci_result[i-1] + fibonacci_result[i-2]
            fibonacci_result.append(fib_sum)
        return fibonacci_result

print(generate_fibonacci(17))

#10
def capitalize_names(s):
    l = []
    for name in s:
        l.append(name.capitalize())      
    return l

print(capitalize_names(['sasha', 'Ihor', 'MARIA', 'lIza']))