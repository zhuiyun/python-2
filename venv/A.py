class Animal(object):


    def __del__(self):
        print("del")


a=Animal()
b=a

del a