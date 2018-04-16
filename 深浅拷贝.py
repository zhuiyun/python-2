#深拷贝
a=[11,22,33]
b=a
# print(id(a))
# print(id(b))

import copy
c=copy.deepcopy(a)
print(id(a))
print(id(c))
print(a is c)
a.append(44)
print(a)
print(b)
print(c)