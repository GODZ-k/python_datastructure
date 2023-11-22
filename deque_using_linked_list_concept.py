class Node:
    def __init__(self, prev=None, next=None, item=None):
        self.prev = prev
        self.item = item
        self.next = next

class Deque:
    def __init__(self, head=None):
        self.head = head
        self.item_count = 0

    def is_empty(self):
        return self.head is None

    def insert_front(self, data):
        n = Node(None, self.head,data)
        if not self.is_empty():
            self.head.prev = n
        self.head = n
        self.item_count += 1

    def insert_rear(self, data):
        n = Node(None, None, data)
        if not self.is_empty():
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            n.prev = temp
            temp.next = n
        else:
            self.head = n
        self.item_count += 1

    def delete_front(self):
        if not self.is_empty():
            if self.head.next is not None:
                self.head = self.head.next
                self.head.prev = None
                self.item_count -= 1
            else:
                self.head = None
        else:
            raise IndexError("No item to delete")

    def delete_rear(self):
        if not self.is_empty():
            if self.head.next is not None:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.prev.next = None
                self.item_count -= 1
            else:
                self.head = None
        else:
            raise IndexError("No item to delete")

    def get_front(self):
        if not self.is_empty():
            return self.head.item
        else:
            raise IndexError("No item")

    def get_rear(self):
        if not self.is_empty():
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            return temp.item
        else:
            raise IndexError("No item")

    def size(self):
        if not self.is_empty():
            return self.item_count
        else:
            raise IndexError("Deque is empty")

# Example usage:
d1 = Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_front(30)
d1.insert_rear(5)

# d1.delete_front()
print("size:", d1.size())
print("Front:", d1.get_front())
print("Rear:", d1.get_rear())
