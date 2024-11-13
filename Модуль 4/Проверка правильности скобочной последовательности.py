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
    
def check_parentheses(s):
  my_stack = Stack()

  matching_brackets = {')': '(', ']': '[', '}': '{'}

  for char in s:
    if char in matching_brackets.values(): 
      my_stack.push(char)
    elif char in matching_brackets:
      if my_stack.is_empty() or my_stack.pop() != matching_brackets[char]:
        return 'Cкобочная последовательность неправильна'
      
  if my_stack.is_empty():
    return 'Cкобочная последовательность правильна'
  else:
    return 'Cкобочная последовательность неправильна'
    

s = input('Напишите текст на проверку скобок: ')
print(check_parentheses(s))

