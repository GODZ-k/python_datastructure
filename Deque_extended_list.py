class Deque(list):
    def is_empty(self):
        return len(self) == 0

    def insert_front(self,data):
        self.insert(0,data)
    def insert_rear(self,data):
      self.append(data)

    def remove_front(self):
        if not self.is_empty():
             self.pop(0)
        else:
            raise IndexError("empty Deque")

    def remove_rear(self):
        if not self.is_empty():
            self.pop()
        else:
            raise IndexError("empty Deque")

    def get_front(self):
        if not self.is_empty():
            return self[0]

        else:
            raise IndexError("empty Deque")

    def get_rear(self):
        if not self.is_empty():
            return self[-1]

        else:
            raise IndexError("empty Deque")

    def size(self):
       if not self.is_empty():
         return len(self)
       else:
         print("empty Deque")


d1=Deque()
d1.insert_front(10)
# d1.insert_front(20)
# d1.insert_front(30)
# d1.insert_front(40)
# d1.insert_front(50)
# d1.remove_rear()
d1.remove_front()
print("size",d1.size())
print("front  item ",d1.get_front())
print("rear item ",d1.get_rear())