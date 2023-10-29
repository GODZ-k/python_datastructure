
class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.item = item
        self.next=next
        self.prev=prev

class DCLL:
    def __init__(self,head=None):
        self.head = head


    def is_empty(self):
        return self.head is None

    def at_first(self,data):
        n=Node(None,data)
        if not self.is_empty():
            n.next=self.head
            n.prev=self.head.prev
            self.head.prev.next=n
            self.head.prev=n
            self.head=n

        else:
            n.prev=n
            n.next=n
            self.head=n

    def at_last(self,data):
        n=Node(None,data)
        if not self.is_empty():
            if self.head.next == self.head:
                n.next=self.head
                n.prev=self.head
                self.head.next=n
                self.head.prev=n
            else:
                n.next=self.head
                n.prev=self.head.prev
                self.head.prev.next=n
                self.head.prev=n
        else:
            n.prev=n
            n.next=n
            self.head=n

    def search(self,data):
        temp=self.head
        if not self.is_empty():
            while temp.item !=data:
                temp=temp.next
            return temp
        else:
            print("list is empty")


    def at_after(self,temp,data):
        n=Node(None,data)
        if not self.is_empty():
            if temp.next == self.head:
                n.next=temp.next
                n.prev=temp
                temp.next=n
                self.head.prev=n
            else:
             n.next=temp.next
             n.prev=temp.next.prev
             temp.next.prev =n
             temp.next=n
        else:
            return False



    def delete_first(self):
        if not self.is_empty():
            if self.head.next == self.head:
                self.head =None
            elif self.head.next.next == self.head:
              self.head=self.head.next
              self.head.prev.next=None
              self.head.prev.prev=None
              self.head.prev= self.head
              self.head.next=self.head
            else:
              self.head.next.prev=self.head.prev
              self.head.prev.next=self.head.next
              self.head.prev=None
              self.head=self.head.next
        else:
            return False


    def delete_last(self):
        if not self.is_empty():
            if self.head.next == self.head:
                self.head = None
            elif self.head.next.next== self.head:
                self.head.next.next=None
                self.head.next.prev = None
                self.head.next = self.head
                self.head.prev = self.head
            else:
                self.head.prev.prev.next=self.head
                self.head.prev=self.head.prev.prev
        else:
            return False

    def delete_item(self,data):
        if not self.is_empty():
            if self.head.next == self.head and self.head.item == data:
                self.head = None
            elif self.head.next.next == self.head:
                if self.head.item == data:
                    self.head= self.head.next
                    self.head.prev.prev=None
                    self.head.prev.next= None
                    self.head.prev=self.head
                    self.head.next= self.head
                elif self.head.next.item== data:
                    self.head.next.next=None
                    self.head.next.prev=None
                    self.head.next=self.head
                    self.head.prev=self.head

            else:
                temp=self.head
                while temp.item !=data:
                    temp=temp.next
                if temp.next == self.head:
                    temp.prev.next= self.head
                    self.head.prev = temp.prev
                    temp.next=None
                    temp.prev=None
                elif temp== self.head:
                    self.head.prev.next=self.head.next
                    self.head.next.prev=self.head.prev
                    self.head.prev=None
                    self.head=self.head.next
                else:
                    temp.prev.next=temp.next
                    temp.next.prev=temp.prev
                    temp.next=None
                    temp.prev=None

        else:
            return False


    def print_all_items(self):
        if not self.is_empty():
            temp=self.head
            while temp.next != self.head:
                print(temp.item , end=" ")
                temp=temp.next
            print(temp.item , end=" ")

        else:
            print("list is empty")



mylist=DCLL()
mylist.at_first(10)
mylist.at_first(20)
mylist.at_first(30)
mylist.at_first(40)
mylist.at_first(50)
mylist.at_last(5)
mylist.at_after(mylist.search(10),15)
mylist.at_after(mylist.search(30),25)
mylist.at_after(mylist.search(5),9)
mylist.delete_first()
mylist.delete_last()
mylist.delete_item(20)
mylist.delete_item(5)
# mylist.delete_item(40)
# mylist.delete_item(40)
mylist.delete_item(40)
mylist.delete_item(30)
mylist.delete_item(15)
# mylist.delete_item(25)
mylist.delete_item(10)
mylist.delete_item(25)
mylist.print_all_items()