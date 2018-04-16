import copy
a=[11,22,33]
b=[44,55,66]
c=[a,b]
print(c)
d=c
print(id(c))
print(id(d))
e=copy.deepcopy(c)
print(e)
print(id(e))