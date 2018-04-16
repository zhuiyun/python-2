# num=100
# def test():
#     num=200
#     print(num)
#     print(locals())
#
# test()
import types
class Person():
    def __init__(self,new_num):
        self.num=new_num

def run(self):
    print(self.num)
a=Person(11)
a.eat=types.MethodType(run,a)
a.eat()
# a.run=run
# a.run(a)
# print(a.num)
# a.num=12
# print(a.num)
# Person.num=13
# print(a.num)