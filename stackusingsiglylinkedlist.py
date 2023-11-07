from singly_linked_list import *
class Stack:
    def __init__(self):
      self.item=SLL()
      self.item_count=0

    def is_empty(self):
        return self.item.is_empty()

    def push(self, data):
        self.item.insert_at_start(data)
        self.item_count +=1

    def pop(self):
        if not self.is_empty():
            self.item.delete_first()
            self.item_count -=1
        else:
            IndexError("list is empty")

    def peek(self):
        return self.item.head.item

    def size(self):
        return self.item_count

s1=Stack()
s1.push(12)
s1.push(13)
s1.pop()
print("last item ",s1.peek())
print("size stack",s1.size())