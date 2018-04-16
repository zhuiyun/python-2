# Test2=type("Test",(),{})
# print(type(Test2()))
# Person=type("P",(),{"num":11})
# print(Person().num)
#
# def printNum(self):
#     print("1111111")
# T=type("Test3",(),{"printNum":printNum})
# T().printNum()
class Animal:
    def eat(self):
        print("eat")

class Dog(Animal):
    pass

wangcai=Dog()
wangcai.eat()
Tom=type("Cat",(Animal,),{})
Tom().eat()
print(Tom.__class__)