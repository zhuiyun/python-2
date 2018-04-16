class Test(object):

    def __init__(self,func):

        print("初始化"+func.__name__)
        self.__func=func
    def __call__(self):
        print("call")
        self.__func()

@Test
def test1():
    print("11111")


test1()


