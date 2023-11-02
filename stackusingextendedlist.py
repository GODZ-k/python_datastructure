class stack(list):
    def is_empty(self):
        return len(self)==0

    def push(self,data):
        self.append(data)

    def pop(self):
        try:
         if not self.is_empty():
          super().pop()
         else:
            return IndexError("list is empty")
        except Exception as e:
            print(e)

    def peek(self):
        try:
         if not self.is_empty():
            return self[-1]
         else:
            return IndexError("list is empty")
        except Exception as e:
            print(e)

    def size(self):
        try:
            if not self.is_empty():
             return len(self)
            else:
                return IndexError("Empty index")
        except Exception as e:
            print(e)

    def res_insert(self,index,data):
        try:
         raise AttributeError(" insert method not allowed")
        except Exception as e:
            print(e)


s1=stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
s1.push(60)
s1.push(70)
s1.push(80)
s1.push(90)
s1.pop()
s1.pop()
s1.res_insert(1,211)

print("last item is" , s1.peek())
print("size of stack is",s1.size())