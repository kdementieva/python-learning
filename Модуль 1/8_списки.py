#1
s = '4 -1 9 3'
l = s.split()
print(sum(map(int, l))) # map преобразует каждую подстроку в целое число и создаёт список

#2
print(l[1::2])

#3
num_list = [10,30,40,50,60]
average = sum(num_list)/len(num_list)
rnd_average = round(average, 3)
print(f'{rnd_average:.3f}') #форматирование строк, для вывода 3 знаков после запятой

#4
s = 'ОРРОРОРООРРРО'
quant_r = s.count('Р')
quant_o = s.count('О')
len_ = len(s)
proc_o = (len_ * quant_o)/100
proc_p = (len_ * quant_r)/100
info_o = f'Процент выпадения Орла: {proc_o}'
info_p = f'Процент выпадения Решки: {proc_p}'
print(info_o)
print(info_p)