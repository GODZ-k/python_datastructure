class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class Queue:
    def __init__(self,head=None,item_count=0):
        self.head=head
        self.item_count=item_count
        # self.rear=rear

    def is_empty(self):
        return self.head is None

    def enqueue(self,data):
        n=Node(data)
        if not self.is_empty():
            n.next=self.head
            self.head =n
        else:
            self.head =n
        self.item_count +=1

    def dequeue(self):
        if not self.is_empty():
            if self.head.next is not None:
                temp=self.head
                while temp.next.next is not None:
                    temp=temp.next
                temp.next=None
            else:
                self.head =None
            self.item_count -=1
        else:
            raise IndexError("queue is empty")

    def get_front(self):
        if not self.is_empty():
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            return temp.item
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


q5=Queue()
q5.enqueue(10)
q5.enqueue(20)
q5.enqueue(30)
q5.enqueue(40)
q5.enqueue(50)
q5.enqueue(60)
q5.dequeue()
print(" Size of queue :",q5.size())
print("front item :",q5.get_front())
print("rear item :",q5.get_rear())





