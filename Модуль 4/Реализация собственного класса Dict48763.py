class MyDict:
  def __init__(self):
    self._items = []

  def __getitem__(self, key):
    for k, value in self._items:
      if k == key:
        return value
    return None

  def __setitem__(self, key, value):
    for i in self._items:
      if i[0] == key:
        self._items[i] = (key, value)
        return
    self._items.append((key, value))

  def __delitem__(self, key):
    self._items = [(k, v) for k, v in self._items if k != key]
      
  def keys(self):
    return [k for k, _ in self._items]
  
  def values(self):
    return [v for _, v in self._items]

  def items(self):
    return self._items[:]

  def __str__(self):
    return "{" + ", ".join(f"{key}: {value}" for key, value in self._items) + "}"
  
  def __contains__(self, key):
    return any(k == key for k, _ in self._items)

  def test(self):
    y = enumerate(self._items)
    print(list(y))

my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30
print(my_dict['name'])  # Вернет 'Alice'
print('city' in my_dict)  # Вернет False
del my_dict['age']
print(my_dict.keys())  # Вернет ['name']
print(my_dict.values())  # Вернет ['Alice']
print(str(my_dict))