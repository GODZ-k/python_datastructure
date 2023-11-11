from singly_linked_list import *

class Queue(SLL):

    def __init__(self):
        super().__init__()
        self.item_count = 0

    def is_empty(self):
        return super().is_empty()

    def enqueue(self,data):
        self.insert_at_start(data)
        self.item_count +=1

    def dequeue(self):
        if not self.is_empty():
            self.delete_last()
            self.item_count -=1
        else:
            raise IndexError("query is empty")

    def get_front(self):
        if not self.is_empty():
            return self.element()
        else:
            raise IndexError("queue is empty")

    def get_rear(self):
        if not self.is_empty():
            return self.head.item
        else:
            raise IndexError("queue is empty")

    def size(self):
        if not self.is_empty():
            return self.item_count
        else:
            raise IndexError("queue is empty")

q4=Queue()
q4.enqueue(10)
q4.enqueue(20)
q4.enqueue(30)
q4.enqueue(40)
q4.enqueue(50)
q4.dequeue()
print(" front item :",q4.get_front())
print(" rear item :", q4.get_rear())
print(" size of queue :", q4.size())
