class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next
class DLL:
    def __init__(self,head=None):
        self.head = head

    def is_empty(self):
        return self.head is None

    def insert_at_start(self,data):
        n=Node(None,data,self.head)
        self.head = n
        self.head.prev=n.next

    def insert_at_end(self,data):
        n=Node(None,data)
        if self.head is None:
            self.head=n
        elif self.head.next is None:
         self.head.next=n
         n.prev=self.head
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            n.prev=temp
            temp.next=n
            # n.next=None

    def search(self,data):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp.next is not None:
                if temp.item == data:
                  return temp
                temp=temp.next

    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            temp.next.prev=n
            temp.next=n
        else:
            print("no data found")



    def print_all_items(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.item,end=" ")
                temp=temp.next

    def delete_first(self):
        self.head=self.head.next
        self.head.prev=None

    def delete_last(self):
        temp=self.head
        if temp is not None:
           while temp.next is not None:
             temp=temp.next
           temp=temp.prev
           temp.next.prev=None
           temp.next=None
        else:
            print("Nothing to delete")


    # def delete_item(self,temp):  # sourcery skip: extract-method
        # if self.head is None:
        #     print("Nothing to delete")

        # elif self.head is temp:
        #     self.head=temp.next
        #     self.head.prev=None
        # elif temp is not None:
        #     temp=temp.prev
        #     temp.next=temp.next.next
        #     temp=temp.next.prev
        #     temp.next.prev=temp.prev
        #     temp.next=None
        #     temp.prev=None

        # else:
        #    temp=temp.prev
        #    temp.next.prev=None
        #    temp.next=None

    def delete_item(self,data):
        # sourcery skip: merge-else-if-into-elif, swap-if-else-branches
        if not self.is_empty():
            if self.head.next == None and self.head.item == data:
               self.head = None
            elif self.head.next.next == None:
               if self.head.item == data:
                   self.head=self.head.next
                   self.head.prev.next =None
                   self.head.prev=None
               elif self.head.next.item == data:
                   self.head.next.prev=None
                   self.head.next=None
            else:
                temp=self.head
                while temp.item !=data:
                    temp=temp.next
                if temp.next == None:
                    temp.prev.next =None
                elif temp== self.head:
                    self.head=temp.next
                    # self.head.prev.next=None
                    temp.next=None
                    self.head.prev = None
                else:
                    temp.prev.next=temp.next
                    temp.next.prev=temp.prev
                    # temp.next=None
                    # temp.prev=None
        else:
            return False









    def __iter__(self):
       return iterator(self.head)


class iterator:
    def __init__(self,head):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration

        data=self.current.item
        self.current=self.current.next
        return data



mylist=DLL()
mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.insert_at_start(40)
mylist.insert_at_end(45)
mylist.insert_at_end(55)
mylist.insert_at_end(65)
mylist.insert_after(mylist.search(55),75)
mylist.insert_after(mylist.search(75),85)
# mylist.delete_item(85)
# mylist.delete_item(85)
# mylist.delete_item(40)
# mylist.delete_item(65)
# mylist.delete_item(65)
mylist.delete_item(65)
# mylist.delete_item(40)
# mylist.delete_item(20)
# mylist.delete_item(20)
mylist.delete_item(85)
mylist.delete_item(40)
# mylist.delete_item(10)
mylist.delete_item(55)

mylist.print_all_items()
# for x in mylist:
#     print(x,end=" ")