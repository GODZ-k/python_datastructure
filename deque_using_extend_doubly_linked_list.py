from doubly_linked_list import *

class Deque(DLL):

    def __init__(self):
        super().__init__()
        self.item_count =0

    def is_empty(self):
        return super().is_empty()
    def insert_front(self,data):
        self.insert_at_start(data)
        self.item_count +=1

    def insert_rear(self,data):
        self.insert_at_end(data)
        self.item_count +=1

    def delete_front(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count -=1
        else:
            raise IndexError("Deque is empty")
    def delete_rear(self):
        if not self.is_empty():
            self.delete_last()
            self.item_count -=1
        else:
            raise IndexError("Deque is empty")

    def get_front(self):
        if not self.is_empty():
            return self.head.item

        else:
            raise IndexError("Deque is empty")

    def get_rear(self):
        if not self.is_empty():
            return self.get_last().item
        else:
            raise IndexError("Deque is empty")

    def size(self):
        return self.item_count



d1=Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_front(30)
d1.insert_front(40)
d1.insert_rear(5)
d1.insert_rear(4)
d1.delete_front()
d1.delete_rear()
print("front",d1.get_front())
print("rear",d1.get_rear())
print("size", d1.size())