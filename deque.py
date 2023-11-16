class Deque:

    def __init__(self):
        self.item = []
    def is_empty(self):
        return len(self.item) == 0

    def insert_rear(self,data):
        self.item.append(data)

    def insert_front(self,data):
        self.item.insert(0,data)

    def delete_front(self):
        if not self.is_empty():
            return self.item.pop(0)
        else:
            raise IndexError("Deque is empty")

    def delete_rear(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("Deque is empty")

    def get_front(self):
        if not self.is_empty():
            return self.item[0]
        else:
            raise IndexError("Deque is empty")

    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("Deque is empty")

    def size(self):
        if not self.is_empty():
            return len(self.item)
        else:
            raise IndexError("Deque is empty")


d1=Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_front(30)
d1.insert_rear(5)
d1.insert_rear(40)
d1.delete_front()
d1.delete_rear()
print("size:",d1.size())
print("front item :",d1.get_front())
print("rear item :",d1.get_rear())