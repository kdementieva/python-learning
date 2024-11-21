<<<<<<< HEAD
def selection_sort(arr):
  for el in range(len(arr)): 
    min_ = el  #определяем начальный минимум
    for i in range(el + 1, len(arr)):
      if arr[i] < arr[min_]: #выбераем мин эл в каждой итерации
        min_ = i  #приписываем новое минимальное значение
    (arr[el], arr[min_]) = (arr[min_], arr[el]) #меняем местами

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
=======
def selection_sort(arr):
  for el in range(len(arr)): 
    min_ = el  #определяем начальный минимум
    for i in range(el + 1, len(arr)):
      if arr[i] < arr[min_]: #выбераем мин эл в каждой итерации
        min_ = i  #приписываем новое минимальное значение
    (arr[el], arr[min_]) = (arr[min_], arr[el]) #меняем местами

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
>>>>>>> eed5f476b3ee324d9277721589fbce6ba5f89b25
print("Отсортированный список:", my_list)