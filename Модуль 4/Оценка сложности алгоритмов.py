#1 Алгоритм проверки наличия дубликатов в массиве.
#O(n^2) - Квадратичная сложность, тк на каждом шаге алгоритм проходит еще раз по списку, чтобы найти дубликат.

def has_duplicates(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

#2 Алгоритм поиска максимального элемента в неотсортированном массиве.
#Также O(n) - Линейная сложность, тк при поиске максимального эл в неотсортированном массиве может потребоваться проверить каждый элемент.

def find_max(arr):
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = val
    return max_val

#3 Алгоритм сортировки выбором (Selection Sort).
#O(n^2) - Квадратичная сложность, тк на каждом шаге алгоритм проходит еще раз по списку, чтобы найти наименьшее число и поставить его на место.

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

#4 Алгоритм быстрой сортировки (Quick Sort).
#Целый алгоритм имеет О(n log n) - Линейно-логарифмическую сложность, тк он использует разделение массива на подмассивы и после сортировки их объединяет
#Само разделение и объединение массивов имеет O(log n) - тк, используется рекурсивное разделение 
#А уже сортировка каждого массива идет за O(n), тк проверяется каждый эл

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

#5 Алгоритм вычисления n-го числа Фибоначчи (рекурсивно).
#O(n^2) - Квадратичная сложность, тк на каждом шаге алгоритм вызывается 2 раза с помощью рекурсии

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
