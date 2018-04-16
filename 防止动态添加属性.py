class Person(object):
    __slots__ = ("name","age")
    def __init__(self,name,age):
        self.name=name
        self.age=age

p=Person("zhuiyun",19)
# p.num=16
# print(p.num)
