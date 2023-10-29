class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self,head=None):
        self.head = head

    def is_empty(self):
        return self.head is None

    def insert_at_start(self,data):
        n=Node(data,self.head)
        self.head=n

    def insert_at_last(self,data):
        n=Node(data)
        if not self.is_empty():
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            print("Empty")

    def search(self,data):
        if not self.is_empty():
            temp=self.head
            while temp is not None:
                if temp.item == data:
                  return temp
                temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
        else:
            print("empty")

    def delete_first(self):
        if self.head is not None:
         self.head=self.head.next
        else:
            print("list is empty")

    def delete_last(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head= None
            print("list is empty")
        else:
         temp=self.head
         while temp.next.next is not None:
            temp=temp.next
         temp.next=None

    def delete_item(self,data):
        if self.head is None:
            pass
        elif self.head.next is None:
         if self.head.item == data:
            self.head=None
        else:
            temp=self.head
            if temp.item == data:
                self.head=temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        if temp.next.next is None:
                            temp.next=None
                        else:
                            temp.next=temp.next.next
                            break
                    temp=temp.next


    def print_all_items(self):
        temp=self.head
        if temp is not None:
            while temp is not None:
              print(temp.item,end=" ")
              temp=temp.next
        else:
            print("Nothing")


    def __iter__(self):
        return SLLIterator(self.head)


class SLLIterator:
    def __init__(self,head):
        self.current=head
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
          raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data



mylist=SLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.insert_at_start(40)
mylist.insert_at_start(50)
mylist.insert_at_start(60)
mylist.insert_at_start(70)
mylist.insert_at_last(390)
mylist.insert_at_last(300)
mylist.insert_after(mylist.search(30),200)
mylist.delete_first()
mylist.delete_first()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_first()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.insert_at_start(40)
mylist.insert_at_start(50)
mylist.insert_at_start(60)
mylist.insert_at_start(70)
mylist.insert_at_last(390)
mylist.insert_at_last(300)
mylist.insert_after(mylist.search(30),200)
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()

mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.insert_at_start(40)
mylist.insert_at_start(50)
mylist.insert_at_start(60)
mylist.insert_at_start(70)
mylist.insert_at_last(390)
mylist.insert_at_last(300)
mylist.insert_after(mylist.search(30),200)
mylist.delete_item(40)
mylist.delete_item(70)
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.insert_at_start(40)
mylist.insert_at_start(50)
mylist.insert_at_start(60)
mylist.insert_at_start(70)
mylist.insert_at_last(390)
mylist.insert_at_last(300)
mylist.insert_after(mylist.search(30),200)
mylist.delete_item(70)
mylist.delete_item(70)
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.delete_last()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.insert_at_start(40)
mylist.insert_at_start(50)
mylist.insert_at_start(60)
mylist.insert_at_start(70)
mylist.insert_at_start(80)
mylist.insert_at_start(90)
mylist.insert_at_start(100)
mylist.delete_item(80)
mylist.delete_item(80)
mylist.delete_item(100)
mylist.delete_item(30)
mylist.delete_item(20)



# mylist.print_all_items()
for x in mylist:
    print(x,end=" ")


