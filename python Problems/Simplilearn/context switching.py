from threading import *;
import time;
class num():
    def num1(self):
        for i in range(0,5):
            print("Number is:",i)
        time.sleep(1)
    def double(self):
        for i in range(0,5):
            print("Double of number:",2*i)
        time.sleep(1)
    def Square(self):
        for i in range(0,5):
            print("Square of a nmber is:",i*i);
        time.sleep(1)
obj=num();

t1=Thread(target=obj.num1)
t2=Thread(target=obj.double)
t3=Thread(target=obj.Square)

t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()
time.sleep(0.2)