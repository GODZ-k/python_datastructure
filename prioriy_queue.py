class Pqueue:

    def __init__(self):
        self.item=[]

    def is_empty(self):
        return len(self.item) == 0

    def push(self,index,data):
        self.item.insert(index,data)

    def pop(self,index):
        if not self.is_empty():
            self.item.pop(index)
        else:
            raise IndexError("Pqueue is empty")

    def size(self):
        return len(self.item)

    def print(self):
        return self.item

p1=Pqueue()
p1.push(1,10)
p1.push(0,20)
p1.push(2,60)
p1.push(3,30)
p1.push(4,40)
p1.push(5,50)
p1.pop(1)
print(" size :",p1.size())
print("items: ",p1.print())