class Queue:
  def __init__(self):
      self.item=[]

  def is_empty(self):
    return len(self.item) == 0

  def enqueue(self,data):
      self.item.append(data)

  def dequeue(self):
    if not self.is_empty():
       return self.item.pop(0)
    else:
        raise IndexError("list is empty")
  def get_front(self):
    if not self.is_empty():
      return self.item[0]
    else:
        raise IndexError("list is empty")
  def get_rear(self):
      if not self.is_empty():
          return self.item[-1]
      else:
          raise IndexError("list is empty")
  def size(self):
      if not self.is_empty():
          return len(self.item)
      else:
          raise IndexError("list is empty")

q1=Queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
q1.enqueue(60)
q1.enqueue(70)
q1.enqueue(80)
q1.dequeue()
q1.dequeue()
print("front item of the queue :",q1.get_front())
print("rear item of the queue :",q1.get_rear())
print("size of the queue :",q1.size())


