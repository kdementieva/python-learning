class Node:
  def __init__(self, value):
    self.value = value #значение узла

    self.outbound = [] #список исходящих рёбер из узла
    self.inbound = [] #список входящих рёбер в узел

  def point_to(self, other):
    self.outbound.append(other)
    other.inbound.append(self)

  def __str__(self):
    return f'Node({self.value})'
    
class Graph:
  def __init__(self, root):
    self._root = root

  def dfs(self, start, visited=None):
    if visited is None:
      visited = []

    if start not in visited:
      print(start, end = ' ')
      visited.append(start)
      for neighbour in start.outbound: #идем по исходящим рёбрам узла
        self.dfs(neighbour, visited)
    

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)

g = Graph(a)
g.dfs(a)