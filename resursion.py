def  f1(n):
    if n ==1:
        return 1
    s=n+f1(n-1)
    return s

r=f1(3)
print(r)

