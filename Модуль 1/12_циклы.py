#1
a = 4
b = 20
for i in range(a, b + 1):
    print(i)

#2
for i in range(2, 201, 2):
    print(i, end=" ")

#3
n = 20
for i in range(1, n):
    print(i ** 2, end=" ")

#4
sum_ = sum(range(100, 501))
print(sum_)

#5
a = int(input('Введите первое целое число: '))
b = int(input('Введите второе целое число: '))
sum_ = 0
quantity = 0
for i in range(a, b + 1):
    quantity += 1
    sum_ += i
print(f'Количество чисел между: {quantity}, их сумма: {sum_}')
    
#6
n = 20
for i in range(n):
    if i < n and i > 0:
        print(i, end=" ")

#7
n = 70
i = 1
while i**2 <= n:
    i += 1
print(i**2)

#8
n = 4784
n = str(n)
first = n[0]
print(first)

#9
n = 28283
stroka = str(n)
sum_ = 0
for i in stroka:
    sum_ += int(i)
print(sum_)

#10
i = 1
summ = 0
while i != '0':
    i = input('Введите число: ')
    summ += int(i)
print(summ)

#11
print('Верно ли, что все элементы последовательности равны между собой?')
l = [49, 49, 49, 49, 49, -22]
i = 0

while True:
    if l[i] < 0:
        print('да')
        break
    elif l[i] != l[0]:
        print('нет')
        break
    i += 1

#12
i = 1
quant = 0
count = 0
while count < 1000:
    i = input('Введите число: ')
    if int(i) == 0:
        break
    elif int(i) >= 30000:
        continue
    elif int(i) % 2 == 0 and int(i) % 7 == 0:
        quant += 1
    count +=1
print(quant)

#13
i = 1
smallest = None
count = 0
while count < 1000:
    i = input('Введите число: ')
    if int(i) == 0:
        break
    elif int(i) >= 30000:
        continue
    elif int(i) % 3 == 0:
        if smallest is None or int(i) < smallest:
            smallest = int(i)
    count +=1
print(smallest)

#14
i = 1
quant = 0
count = 0
while count < 1000:
    i = input('Введите число: ')
    if int(i) == 0:
        break
    elif int(i) >= 30000:
        continue
    elif int(i) % 5 == 0 or int(i) % 7 == 0:
        quant += 1
    count +=1
print(quant)

#15
days = int(input('Введите количество дней: '))
if 1 <= days <= 31:
    count = 0
    sum_ = 0
    plus_temp = 0
    while count <= days - 1:
        temp = int(input('Введите температуру: '))
        sum_ += temp
        count += 1
        if temp > 0:
            plus_temp += 1
    if plus_temp >= 5:
        print(sum_ / count, 'YES')
    else:
        print(sum_ / count, 'NO')
else:
    print('Неправильное значение!')

#16
quant = int(input('Введите кол-во чисел: '))
if quant < 1000:
    count = 0
    smallest = None
    while count <= quant - 1:
        i = int(input('Введите число: '))
        if i > 30000:
            continue
        elif i % 2 == 0:
            if smallest is None or i < smallest:
                smallest = i
        count += 1
    print(smallest)
else:
    print('Неправильное значение!')

#17
cars = int(input('Введите количество машин: '))
if 1 <= cars <= 30:
    speed = 0
    count = 0
    fast_car = 0
    smallest = None
    while count <= cars - 1:
        speed = float(input('Введите cкорость: '))
        if 1 <= speed <= 300:
            speed_rnd = round(speed)
            if speed_rnd > 80:
                fast_car += 1
            if smallest is None or speed_rnd < smallest:
                smallest = speed_rnd
        else:
            print('Неправильное значение!')
            continue
        count += 1
    if fast_car > 0:
        print(smallest, 'YES')
    else:
        print(smallest, 'NO')
else:
    print('Неправильное значение!')
    