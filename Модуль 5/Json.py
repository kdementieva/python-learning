import json
import csv

def get_data():
  data = []
  with open('prices.csv', 'r', encoding='utf-8') as csfile:
    reader = csv.DictReader(csfile)
    for row in reader:
      data.append({
        'Наименование товара' : row['Наименование товара'],
        'Количество товара' : int(row['Количество товара']),
        'Цена/шт' : int(row['Цена/шт'])
      })
  return data

def new_json(data):
  return json.dumps(data, ensure_ascii=False, indent=4) #ensure_ascii=False сохраняет кириллицу, indent=4 отступ в 4 пробела 

print(new_json(get_data()))
data = get_data()
print(json.dumps(data, ensure_ascii=False)) #или в таком виде?