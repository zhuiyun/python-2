from collections import Iterator

a=[x for x in range(10)]
print(a)
b=(x for x in  range(10))
print(b)
for temp in b:
    print(temp)

print(isinstance("100",Iterator))
print(isinstance([],Iterator))