import random
import time
import threading

WELCOME_MESS = '''Добро пожаловать в "Подземелье приключений"!\n
Ты — отважный искатель сокровищ, готовый спуститься в мрачные глубины. 
В комнатах подземелья тебя ждут драгоценности, смертельные ловушки и опасные монстры. 
Твоя цель — собрать как можно больше сокровищ и выйти, сохранив жизни.\n
Готов испытать свою смелость?\n
Удачи, герой!\n
Нажми клавишу "y", чтобы начать игру, "n" для выхода или "i" для прочтения инструкции'''

BYE_MESS = '''Спасибо за игру в "Подземелье приключений"! 
Надеемся, ты получил море впечатлений и адреналина. 
Возвращайся за новыми сокровищами и испытаниями в любое время!\n
До новых встреч, герой!'''

INSTRUCTION_MESS = '''Как играть:\n
Используй клавиши для перемещения:\n
w — движение вперед.\n
a — движение влево.\n
s — движение назад.\n
d — движение вправо.\n
Нажми i, чтобы вывести эту инструкцию на экран в любой момент.\n
Чтобы выйти из игры в любой момент, нажми e.\n
Описание комнат:\n
Сокровищница: приносит дополнительные очки.\n
Ловушка: теряешь одну жизнь.\n
Монстр: есть шанс победить и остаться целым или потерять одну жизнь.\n
Цель игры: собрать 5 очков, 
не потеряв все свои жизни. Первый уровень состоит 
из 3 комнатных испытаний. Пройди их все, чтобы продолжить приключение!\n '''

BAD_MOVE_MESS = 'Неверная команда! Используйте только w, a, s, d для передвижения, e для выхода из игры или i для прочтения инструкции.'

TREASURE_MESS = '''Вы вошли в комнату, и перед вами появился сундук с сокровищами. Внутри блестят золотые монеты! Хотите открыть сундук?\n
Нажми клавишу "y", чтобы открыть сундук или "w", чтобы идти дальше.'''

TRAP_MESS = '''Вы вошли в комнату, и тут же услышали странный звук. Внезапно пол под вами начинает опускаться, и вы попали в ловушку! Что будете делать?\n
Нажми клавишу "y", чтобы попробовать избежать ловушки\n 
Осторожно, у Тебя мало времени!'''

MONSTER_MESS = '''Вы вошли в комнату, и перед вами появился ужасный монстр! Он рычит и готов напасть. Что будете делать?\n
Нажмите "y", чтобы сразиться, или любую другую клавишу, чтобы убежать.'''

NEXT_LEVEL_MESS = '''Поздравляем! Вы прошли первый уровень.\n
У Вас {lives} жизней и {points} очков.'''

class Player:
  def __init__(self, lives, points):
    self.lives = lives
    self.points = points
    self.player_input = ''
    self.input_received = False
    self.stop_event = threading.Event()
    
  def treasure_room(self, treasure):
    print(TREASURE_MESS)
    s = input().lower()
    if s == 'y':
      self.points += treasure
      return f'Вы нашли сокровище! Очки: +{treasure}. Всего очков: {self.points}'
    else:
      return 'Вы решили не брать сокровище и покинули комнату.'
    
  def countdown(self):
    for i in range(3, 0, -1):
      if self.stop_event.is_set():
        return
      print(i)
      time.sleep(1)
    if not self.stop_event.is_set():
      print('Ловушка сработала!')
      self.stop_event.set()
  
  def get_input(self):
      self.player_input = input().lower()
      self.input_received = True
      self.stop_event.set()
    
  def trap_room(self):
    print(TRAP_MESS)

    countdown_thread = threading.Thread(target=self.countdown) 
    input_thread = threading.Thread(target=self.get_input)

    countdown_thread.start()
    input_thread.start()

    countdown_thread.join()
    input_thread.join()

    if self.input_received and self.player_input == 'y' and not self.stop_event.is_set():
      return 'Вы выбрались! Жизни не потеряны.'
    elif self.stop_event.is_set() and (not self.input_received or self.player_input != 'y'):
      self.lives -= 1
      return f'Вы не успели выбраться! Ловушка сработала. Осталось жизней: {self.lives}' 
    else:
      self.lives -= 1
      return f'Вы не выбрались из ловушки. Осталось жизней: {self.lives}'

  def monster_room(self):
    print(MONSTER_MESS)
    
    if input() == 'y':
      chance = random.randint(1, 100)
      print(f'Ваш шанс на победу: {chance}%\n')
      if chance > 50: 
        return 'Вы победили монстра! Жизни не потеряны.'
      else:
        self.lives -= 1
        return f'Монстр вас ранил! Осталось жизней: {self.lives}'
    else:
      if len(all_in_rooms) >= 2:
        return f'Вы вернулись в {all_in_rooms[-2]}'
      return 'Вы решили отступить и вернулись назад.'

class Room:
  def __init__(self):
    self.name = None

  def get_room(self, player):
    room_types = ['treasure', 'trap', 'monster']
    chosen_room = random.choice(room_types)
    if chosen_room == 'treasure':
      self.name = 'treasure'
      treasure = random.randint(1, 5)
      return player.treasure_room(treasure)
    elif chosen_room == 'trap':
      self.name = 'trap'
      return player.trap_room()
    elif chosen_room == 'monster':
      self.name = 'monster' 
      return player.monster_room()
      

def get_move(s):
  if s == 'y':
    return 'Подтверждено, игра продолжается.'
  elif s in 'en':
    print(BYE_MESS)
    exit()
  elif s in 'wad':
    return f'Вы переместились в направлении {s.upper()}.'
  elif s == 's':
    return 'Вы переместились назад.'
  elif s == 'i':
    return INSTRUCTION_MESS
  else:
    return BAD_MOVE_MESS


player1 = Player(3, 0)
all_in_rooms = []

print(WELCOME_MESS)
while player1.lives > 0 and len(all_in_rooms) < 4:
    s = input('Ваш ход: ').lower()
    move = get_move(s)
    if s in 'ien':
      print(move)
      continue
    if move.startswith('Неверная команда'):
      print(move)
      continue
    
    room = Room()
    room_result = room.get_room(player1)
    all_in_rooms.append(room.name)
    print(room_result)

    if player1.lives <= 0:
      print('Вы потеряли все жизни! Игра окончена.')
      break

if player1.lives > 0:
  print(NEXT_LEVEL_MESS.format(lives = player1.lives, points = player1.points))
  print(all_in_rooms)



