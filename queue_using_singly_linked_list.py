from singly_linked_list import *

class Queue:

    def __init__(self):
        self.item = SLL()
        self.item_count = 0

    def is_empty(self):
        return self.item.is_empty()

    def enqueue(self,data):
        self.item.insert_at_start(data)
        self.item_count +=1

    def dequeue(self):
        if not self.is_empty():
            self.item.delete_last()
            self.item_count -=1
        else:
            raise IndexError("No more items to dequeue")

    def get_front(self):
        if not self.is_empty():
            return self.item.element()

        else:
            raise IndexError("queue is empty")

    def get_rear(self):
        if not self.is_empty():
            return self.item.head.item
        else:
            raise IndexError("queue is empty")

    def size(self):
        if not self.is_empty():
            return self.item_count
        else:
            raise IndexError("queue is empty")

q3=Queue()
q3.enqueue(10)
q3.enqueue(20)
q3.enqueue(30)
q3.enqueue(40)
q3.enqueue(50)
q3.enqueue(60)
q3.dequeue()
print(" front item :",q3.get_front())
print(" rear item :", q3.get_rear())
print(" size of queue :", q3.size())