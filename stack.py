class Stack:
    def __init__(self):
        self.item = []

    def is_emplty(self):
        return len(self.item) == 0

    def push(self, data):
        self.item.append( data )

    def pop(self):
        if not self.is_emplty():
         return self.item.pop()
        else:
            raise IndexError("stack is empty")

    def peek(self):
        if not self.is_emplty():
         return self.item[-1]
        else:
            raise IndexError("stack is empty")

    def size(self):
        return len(self.item)


mystack=Stack()
mystack.push(12)
mystack.push(13)
mystack.push(14)
mystack.push(15)
mystack.push(16)
print(" removed item is :", mystack.pop())
print(" removed item is :", mystack.pop())
print("last element of stack is :" , mystack.peek())
print(" size of the stack is :" , mystack.size())