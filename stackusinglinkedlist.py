class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Stack:
    def __init__(self,head=None,item_count=0):
        self.head=head
        self.item_count=item_count

    def is_empty(self):
        return self.head is None


    def push(self,data):
      n=Node(data)
      if not self.is_empty():
          n.next=self.head
          self.head=n
      else:
          self.head=n
      self.item_count +=1



    def pop(self):
        if not self.is_empty():
            if self.head.next is None:
                self.head = None
            else:
                data=self.head.item
                self.head=self.head.next
                self.item_count -=1
                return data


        else:
            raise IndexError("list is empty")

    def peek(self):
        if not self.is_empty():
            return self.head.item
        else:
            raise IndexError("list is empty")

    def size(self):
        return self.item_count



s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
s1.push(60)
print("deleted item :", s1.pop())
print("deleted item :", s1.pop())
print("deleted item :", s1.pop())
print("last item of the stack is :",s1.peek())
print("size of the stack is :",s1.size())