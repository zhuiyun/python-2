# def test():
#     print("test")
#
# # test()
# b=test
# b()
# print(test)
# def test(number):
#     print("1")
#     def test_in(number2):
#         print("2")
#         print(number+number2)
#
#     print("3")
#     return test_in
#
# ret=test(200)
# ret(2)

def line_conf(a,b):
    def line(x):
        return a*x+b
    return line

line1=line_conf(1,2)
line2=line_conf(4,5)
print(line1(5))
print(line2(5))