# print first n natural numbers

# def printn(n):
#     if n>0:
#         printn(n-1)
#         print(n)

# r=printn(10)


#print n netural no in reverse mode

# def printm(n):
#     if n>0:
#         print(n)
#         printm(n-1)

# r=printm(10)

# print first n add natural no

# def printn(n):
#     if n>0:
#         printn(n-1)
#         print(2*n-1)

# r=printn(10)

# print first n add no in reverse

# def printn(n):
#     if n>0:
#         print(2*n-1)
#         printn(n-1)
# r=printn(10)


# print first n even no

# def printn(n):
#     if n>0:
#         printn(n-1)
#         print(2*n)

# r=printn(10)

# print first n even no in reverse

# def printn(n):
#     if n>0:
#         print(2*n)
#         printn(n-1)

# r=printn(10)

# sum of first n natural numbers

# def printn(n):
#     if n == 1:
#         return 1
#     s=n+printn(n-1)
#     return s

# r=printn(5)
# print(r)

#sum of n odd no

# def sum(n):
#     if n == 1:
#         return 1
#     return 2*n-1 + sum(n-1)

# r=sum(6)
# print(r)

# sum of first n even no

# def sum(n):
#     if n == 1:
#         return 2
#     s=2*n + sum(n-1)
#     return s

# r=sum(5)
# print(r)


# calculate factorial

# def fac(n):
#     if n == 0:
#         return 1
#     s= n* fac(n-1)
#     return s

# r=fac(3)
# print(r)

# sum of square of n no

def sum(n):
    if n == 1:
        return 1
    s= n*n + sum(n-1)
    return s

r=sum(2)
print(r)