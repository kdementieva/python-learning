class Stack:
  def __init__(self):
    self.items = []

  def is_empty(self):
    return len(self.items) == 0

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if not self.is_empty():
      return self.items.pop()
    else:
      raise IndexError("Стек пуст")

  def peek(self):
    if not self.is_empty():
      return self.items[-1]
    else:
      raise IndexError("Стек пуст")

  def size(self):
    return len(self.items)

def operator(char, a, b):
    if char == '+':
      return a + b
    if char == '-':
      return a - b
    if char == '*':
      return a * b
    if char == '/':
      return a / b



def rpn(s):
  operand_stack = Stack()
  tokens = s.split()
  for token in tokens:
    if token.isdigit():
      operand_stack.push(float(token))
    else:
      b = operand_stack.pop()
      a = operand_stack.pop()
      result = operator(token, a, b)
      operand_stack.push(result)
  return operand_stack.pop()


    

s = input('Введите обратную польскую запись: ')
print(rpn(s))
