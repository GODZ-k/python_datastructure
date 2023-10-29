class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class CLL:
    def __init__(self,last= None):
        self.last=last

    def is_empty(self):
        return self.last is None

    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            self.last=n
            n.next=n
        else:
            n.next=self.last.next
            self.last.next=n

    def insert_at_end(self,data):
        n=Node(data)
        if self.is_empty():
             self.last=n
             n.next=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n

    def search(self,data):
        temp=self.last
        while temp.next != None:
            if temp.item == data:
              return temp

            temp=temp.next


    def insert_after(self,temp, data):
        n=Node(data)
        if not self.is_empty():
           n.next=temp.next
           temp.next=n
        else:
            return False

    def delete_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last =None

            elif self.last.next ==self.last:
                self.last.next = self.last
            else:
               self.last.next=self.last.next.next
        else:
            return False

    def delete_last(self):
        if not self.is_empty():
            temp=self.last
            while temp.next != self.last:
                temp=temp.next
            self.last=temp
            temp.next = temp.next.next
        else:
            return False

    def delete_item(self,data):
        if not self.is_empty():
            if self.last.next == self.last and self.last.item == data:
                self.last = None
            elif self.last.next.next == self.last:
                if self.last.item == data:
                    self.last=self.last.next
                else:
                    self.last.next.next=None
            else:
                temp=self.last
                while temp.next.item != data:
                    temp=temp.next
                temp.next=temp.next.next
        else:
            return False

    # def __iter__(self):
    #     return Iterator(self.last)


# class Iterator:
#     def __init__(self,last):
#         self.current=last

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if not self.current:
#             raise StopIteration
#         data=self.current.item
#         self.current=self.current.next
#         return data







    def print_all_items(self):
        if self.last is None:
            print("No items")
        else:
            temp=self.last.next
            while temp != self.last:
                print(temp.item, end=" ")
                temp=temp.next





mylist=CLL()
mylist.insert_at_start(10)
mylist.insert_at_start(10)

mylist.insert_at_start(20)
mylist.insert_at_start(30)
mylist.insert_at_start(40)
mylist.insert_at_start(50)
mylist.insert_at_start(60)
mylist.insert_at_start(70)
mylist.insert_at_end(100)
# mylist.search(10)
mylist.insert_after(mylist.search(70),80)
mylist.insert_after(mylist.search(10),85)
mylist.insert_after(mylist.search(100),95)
mylist.insert_at_start(55)
mylist.insert_at_start(105)
mylist.insert_at_end(5)
mylist.insert_at_end(5)
mylist.insert_at_end(51)
mylist.insert_at_end(51)
mylist.insert_at_end(52)
mylist.delete_first()
mylist.delete_last()
mylist.delete_last()
mylist.delete_item(55)
mylist.delete_item(5)
mylist.delete_item(20)
mylist.insert_at_start(70)
mylist.insert_at_start(70)
mylist.print_all_items()

# for x in mylist:
#     print(x,end=" ")