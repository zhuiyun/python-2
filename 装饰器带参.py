def func_arg(arg):
    def func(functionName):
        def func_in():
            print("---记录日志")
            print(arg)
            functionName()
        return func_in
    return func

@func_arg("hheheh")
def test():
    print("zhuiyun")

test()