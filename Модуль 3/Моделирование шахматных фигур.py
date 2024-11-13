from abc import ABC, abstractmethod

class ChessPiece(ABC):
  def __init__(self, color):
    if color not in ('белый', 'черный'):
        raise ValueError('Цвет должен быть "белый" или "черный"')
    self.color = color
    
  @abstractmethod
  def get_possible_moves(self, position, board):
      pass

class Pawn(ChessPiece):
  def get_possible_moves(self, position, board):
    row, col = position
    moves = []

    if self.color == 'белый':
      forward_moves = [(row, col + 1)]
      if row == 1:
        forward_moves.append((row, col + 2))
    else:
      forward_moves = [(row, col - 1)]
      if row == 6:
        forward_moves.append((row, col - 2))

    moves.extend([move for move in forward_moves if board.is_on_desk(move)])

    if self.color == 'белый':
      capture_moves = [(row + 1, col - 1), (row + 1, col + 1)]
    else:
      capture_moves = [(row - 1, col - 1), (row - 1, col + 1)]

    moves.extend([move for move in capture_moves if board.is_on_desk(move)])
    return moves

class Rook(ChessPiece):
  def get_possible_moves(self, position, board):
    row, col = position
    moves = []

    for i in range(8):
      if i != row and board.is_on_desk((i, col)):
        moves.append((i, col))
      if i != col and board.is_on_desk((row, i)):
        moves.append((row, i))
    return moves

class Bishop(ChessPiece):
  def get_possible_moves(self, position, board):
    row, col = position
    moves = []
    for i in range(1, 8):
      potential_moves = [
        (row + i, col + i), (row - i, col - i),
        (row + i, col - i), (row - i, col + i)
      ]
      moves.extend([move for move in potential_moves if board.is_on_desk(move)]) 

    return moves

class ChessBoard:
  def __init__(self):
    self.horizontal = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    self.vertical = [1, 2, 3, 4, 5, 6, 7, 8]
    
  def position_to_coordinates(self, position):
    column, row = position[0], int(position[1])
    x = self.horizontal.index(column)
    y = row - 1
    return x, y

  def coordinates_to_position(self, coordinates):
    x, y = coordinates
    if 0 <= x < 8 and 0 <= y < 8:
      return f'{self.horizontal[x]}{self.vertical[y]}'
    else:
      return None

  def is_on_desk(self, coordinates):
    x, y = coordinates
    return 0 <= x < 8 and 0 <= y < 8

board = ChessBoard()

pawn = Pawn('белый')
rook = Rook('черный')
bishop = Bishop('белый')

pawn_position = board.position_to_coordinates('B2')
rook_position = board.position_to_coordinates('A8')
bishop_position = board.position_to_coordinates('C1')

print('Pawn moves:', [board.coordinates_to_position(move) for move in pawn.get_possible_moves(pawn_position, board)])
print('Rook moves:', [board.coordinates_to_position(move) for move in rook.get_possible_moves(rook_position, board)])
print('Bishop moves:', [board.coordinates_to_position(move) for move in bishop.get_possible_moves(bishop_position, board)])
