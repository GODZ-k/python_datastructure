class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.priority=priority
        self.next=next

class Priority:
    def __init__(self):
        self.head=None
        self.item_count=0

    def is_empty(self):
        return self.head ==  None


    def push(self,data,priority):
        n=Node(data,priority)
        if self.head is None or priority < self.head.priority:
            n.next=self.head
            self.head=n
        else:
            temp=self.head
            while temp.next is not None and temp.next.priority <= priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.item_count +=1

    def pop(self):
        if self.is_empty():
            raise IndexError("priority queue is empty")

        else:
            data=self.head.item
            self.head=self.head.next
            self.item_count -=1
            return data

    def size(self):
        return self.item_count

    def printitem(self):
        temp=self.head
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next


p=Priority()
p.push(12,1)
p.push(22,2)
# p.push(32,)
p.push(42,4)
p.push(40,5)
p.push(32,3)
p.push(39,6)
p.push(33,7)
p.pop()
# print("all items :",p.print())
print("size:", p.size())
p.printitem()