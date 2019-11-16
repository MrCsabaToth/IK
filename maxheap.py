#MAXHEAP
class PriorityQueue:
  def __init__(self):
    self.A = ['SENTINEL']
    self.size = 0

  def parent(self, i): #Index of parent for node i
    if i >= 1 and i <= self.size:
      return i / 2
    else:
      return -1 #There is no parent

  def leftchild(self, i):
    if i >= 1 and 2*i <= self.size:
      return 2*i
    else:
      return -1

  def rightchild(self, i):
    if i >= 1 and 2*i+1 <= self.size:
      return 2*i + 1
    else:
      return -1

  def insert(self, key):
    self.A.append(key)
    self.size += 1
    curr = self.size #index of the element right now as it is being bubbled up
    while self.parent(curr) != -1 and self.A[self.parent(curr)] < self.A[curr]:
      (self.A[self.parent(curr)],self.A[curr]) = (self.A[curr],self.A[self.parent(curr)])
      curr = self.parent(curr)

  def sink(self,i):
    if i < 1 or i > self.size:
      return
    left = self.leftchild(i)
    right = self.rightchild(i)
    if left == -1:
      return
    if right == -1:
      largerchild = left
    else:
       if self.A[left] > self.A[right]:
         largerchild = left
       else:
          largerchild = right
    if self.A[i] < self.A[largerchild]:
      #swap the two to sink the heavier element down
      (self.A[i],self.A[largerchild]) = (self.A[largerchild],self.A[i])
      self.sink(largerchild)

  
