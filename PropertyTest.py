class Money(object):
    def __init__(self):
        self.__money=100

    def setMoney(self,moneyTemp):
        print("set")
        self.__money=moneyTemp

    def getMoney(self):
        print("get")
        return self.__money

    money=property(getMoney,setMoney)

m=Money()
m.money=1000
print(m.money)