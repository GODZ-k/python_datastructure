from singly_linked_list import *

class Stack(SLL):
    def __init__(self):
       super().__init__()
       self.item_count =0

    def is_empty(self):
       return super().is_empty()

    def push(self,data):
        self.insert_at_start(data)
        self.item_count +=1

    def pop(self):
        if not self.is_empty():
            self.delete_first()
            self.item_count -=1
        else:
            raise IndexError("list is empty")

    def peek(self):
        if not self.is_empty():
            return self.head.item
        else:
            raise IndexError("list is empty")

    def size(self):
        if not self.is_empty():
            return self.item_count
        else:
            raise IndexError("list is empty")

s1=Stack()
s1.push(12)
s1.push(13)
s1.push(14)
s1.push(15)
s1.pop()
print("last item",s1.peek())
print("size of stack",s1.size())
