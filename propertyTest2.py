class Money(object):
    def __init__(self):
        self.__money=100

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self,num):
        self.__money=num

m=Money()
m.money=1000
print(m.money)