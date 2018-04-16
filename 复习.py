a=[x*2 for x in range(100)]
print(a)
b=(x*2 for x in range(100))
print(b)
print(b.__next__())
print(b.__next__())
c=12
d=13
c,d=d,c
print(c)
print(d)