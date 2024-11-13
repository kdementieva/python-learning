s = '123+(d+(a+b)+12)=22'
new_s = s.replace('2', 'two')
print(new_s)
star_first = s.find('(')
star_last = s.rfind(')')
result = s[:star_first] + '*' + s[star_first:star_last+1] + '*' + s[star_last+1:]
print(result)
