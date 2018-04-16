import copy
a=[1,2,3]
b=[4,5,6]
c=(a,b)
e=copy.copy(c)
print(c)
print(id(c))
print(id(e))
