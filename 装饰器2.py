


def func1(funcName):
    print("func")

    def func_in():
        print("func2")
        funcName()
        print("func2")
        print("func3")
    print("func4")
    return func_in
@func1
def test():
    print("-----test-----")
test()

