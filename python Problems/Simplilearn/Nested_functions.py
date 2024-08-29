def hello(name):
    print("It is outer function")
    def print_name(name):
        print("It is inner function")
        name();
    return print_name(name)

def Balaji():
    print("It is another function")


hello(Balaji)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#Another method of creating class
B=type('BaseClass',(object,),{})
C1=type('C1',(B,),{"Val":5})
C2=type('C2',(B,),{"val":10})
obj=C1()
print(obj.Val)
onj2=C2()
print(onj2.val)
