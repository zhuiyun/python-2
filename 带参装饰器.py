def func(funcName):
    print("fun1")
    def func_in(a,b):
        print("func2")
        funcName(a,b)
        print("func3")
    print("func4")
    return func_in

@func
def test(a,b):
    print("%s+++++%s"%(a,b))

test(11,12)