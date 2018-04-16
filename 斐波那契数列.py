# def createNum(num):
#     a,b=0,1
#     print("start")
#     for i in range(num):
#         yield b
#         a,b=b,a+b
#     print("stop")
#
# a=createNum(9)
# for i in a:
#     print(i)

def test():
    i=0
    while i<5:
        temp=yield i
        print("----%s"%temp)
        i+=1

t=test()

print(t.__next__())

print(t.__next__())
print(t.__next__())
print(t.__next__())
print(t.send("hhhh"))