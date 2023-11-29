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

def printn(n):
    if n>0:
        print(2*n)
        printn(n-1)

r=printn(10)