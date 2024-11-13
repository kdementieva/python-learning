def bubble_sort(arr):
  for i in range(len(arr) - 1, 0, -1): #контролирует кол-во проходов по списку
    for el in range(i):  #проходит по каждому эл
      if arr[el] > arr[el + 1]:
        arr[el], arr[el + 1] = arr[el + 1], arr[el]
      
  

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Отсортированный список:", my_list)