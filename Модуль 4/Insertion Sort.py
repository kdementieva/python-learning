def insertion_sort(arr):
  for el in range(1, len(arr)): #начинаем со второго эл
    sec_el = arr[el] #переменная второго эл
    j = el - 1 #индекс предыдущего эл
    while j >= 0 and sec_el < arr[j]: #продолжаем пока индекс не вышел за пределы списка и пока 2эл меньше 1
      arr[j + 1] = arr[j]  #перемещаемся влево
      j -= 1 #переходим к след эл
    arr[j + 1] = sec_el #ставим второй эл на правильную позицию

  

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)
print("Отсортированный список:", my_list)