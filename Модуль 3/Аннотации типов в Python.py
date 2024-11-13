import math
import doctest

class WinDoor:
  """
  Класс, представляющий площадь только окон и дверей.
  """
  def __init__(self, x: int | float, y: int | float) -> None:
    """
    Создает площадь двери или окна.

    :param x: int | float: Высота двери или окна
    :param y: int | float: Ширина двери или окна
    """
    self.square: int | float = x * y

class Room:
  """
  Класс, представляющий площадь комнаты и расчёт необходимых обоев.
  """
  def __init__(self, width: int | float, length: int | float, height: int | float) -> None:
    """
    Создает объект комнаты с заданными параметрами.

    :param width: int | float: Ширина комнаты.
    :param length: int | float: Длина комнаты.
    :param height: int | float: Высота комнаты.
    """
    self.width = width
    self.length = length
    self.height = height
    self.wd: list[WinDoor] = []
 
  def add_wd(self, w: int | float, h: int | float) -> None:
    """
    Добавляет объект окна или двери к комнате.
      
    :param w: int | float: Ширина окна или двери.
    :param h: int | float: Высота окна или двери.
    """
    self.wd.append(WinDoor(w, h))

  def total_surface(self) -> int | float:
    """
    Вычисляет общую площадь стен комнаты.

    :return: int | float: Общая площадь стен комнаты.
    """
    return 2 * self.height * (self.width + self.length)

  def work_surface(self) -> int | float:
    """
    Вычисляет площадь стен комнаты за вычетом окон и дверей.

    :return: int | float: Площадь стен для оклейки обоями.
    >>> room = Room(6, 3, 2.7)
    >>> room.add_wd(1, 1)
    >>> room.add_wd(1, 1)
    >>> room.add_wd(1, 2)
    >>> room.work_surface()
    44.6
    """
    sum_wd = sum(wd.square for wd in self.wd)
    return self.total_surface() - sum_wd
    
  def wallpaper_quant(self, width_of_stripe: int | float, length_of_roll: int | float) -> int:
    """
    Рассчитывает количество рулонов обоев, необходимых для комнаты.
        
    :param width_of_stripe: int | float: Ширина одного полотнища обоев.
    :param length_of_roll: int | float: Длина одного рулона обоев.
    :return: int: Количество рулонов обоев.
    >>> room = Room(6, 3, 2.7)
    >>> room.wallpaper_quant(0.53, 10)
    12
    """
    perimeter = 2 *(self.length + self.width)
    wallpaper_stripes = math.ceil(perimeter / width_of_stripe)  
    stripes_quant = math.floor(length_of_roll / self.height)          
    return math.ceil(wallpaper_stripes / stripes_quant)

def get_positive_int(x: str) -> int:
  """
  Запрашивает положительное целое число у пользователя.

  :param prompt: str: Сообщение для запроса.
  :return: int: Положительное целое число.
  """
  while True:
    try:
      value = int(input(x))
      if value > 0:
        return value
      else:
        print('Введите положительное число.')
    except ValueError:
      print('Некорректное значение. Попробуйте снова.')

def get_positive_float(x: str) -> float:
  """
  Запрашивает положительное число у пользователя.

  :param prompt: str: Сообщение для запроса.
  :return: float: Положительное число с плавающей запятой.
  """
  while True:
    try:
      value = float(input(x))
      if value > 0:
        return value
      else:
        print('Введите положительное число.')
    except ValueError:
        print('Некорректное значение. Попробуйте снова.')

def get_windoor(room: Room, quant: int) -> None:
  """
  Запрашивает у пользователя размеры окон и дверей и добавляет их к комнате.

  :param room: Room: Объект комнаты.
  :param quant: int: Количество окон и дверей.
  """
  for i in range(quant):
    while True:
      try:
        x = float(input(f'Введите высоту окна/двери {i + 1}: '))
        y = float(input(f'Введите ширину окна/двери {i + 1}: '))
        if x > 0 and y > 0:
          room.add_wd(x, y)
          break
        else:
          print('Введите положительные значения для высоты и ширины.')
      except ValueError:
        print('Некорректное значение. Попробуйте снова.')


doctest.testmod()
width = get_positive_float('Введите ширину комнаты: ')
length = get_positive_float('Введите длину комнаты: ')
height = get_positive_float('Введите высоту комнаты: ')
r1 = Room(width, length, height)

quant = get_positive_int('Введите сколько окон и дверей в комнате: ')
get_windoor(r1, quant)

print(f'Площадь оклеиваемой поверхности: {r1.work_surface()}')

wallpaper_width = get_positive_float('Введите ширину обоев: ')
wallpaper_lenght = get_positive_float('Введите длину рулона: ')
print(f'Количество необходимых рулонов: {r1.wallpaper_quant(wallpaper_width, wallpaper_lenght)}')