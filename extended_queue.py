class Queue(list):
    def is_empty(self):
        return len(self) == 0

    def enqueue(self,data):
        self.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.pop(0)
        else:
            raise IndexError("queue is empty")

    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            raise IndexError("queue is empty")

    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("queue is empty")

    def size(self):
        if not self.is_empty():
            return len(self)
        else:
            raise IndexError("queue is empty")


q2=Queue()
q2.enqueue(10)
q2.enqueue(20)
q2.enqueue(30)
q2.enqueue(40)
q2.dequeue()
print(" front item of queue :", q2.get_front())
print(" rear item of queue :", q2.get_rear())
print(" size of queue :", q2.size())
