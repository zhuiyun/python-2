def w1(func):
    print("正在装饰")
    def inner():
        print("验证权限")
        if(False):
            func()
        else:
            print("没有权限")
    return inner


@w1
def f1():
    print("f1")

def f2():
    print("f2")


# f1()