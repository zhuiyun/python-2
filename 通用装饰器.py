def func(funcName):
    print(1)
    def inner(*args,**kwargs):
        print(2)
        return funcName(*args,**kwargs)
        print(3)
        
    print(4)
    return inner

@func
def test(a,b):
    print("test+---%s+++++%s"%(a,b))
    return "hh"

ret=test(11,222)
print(ret)