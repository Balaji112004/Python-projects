from threading import *;
#METHOD-1
#Using function
def show():
   print("Child thread")
t=Thread(target=show())
t.start();
print("Parent Thread")
print("____________________________________________________________________")
#Important note:All program will be run at parent thread
#If we nedd ,we can make use of child thread

#METHOD-2
#Using class
class bhavan(Thread):
   def run(self):
      for i in range(5):
         print("\nChild thread is executed")
t=bhavan();
t.start()
for i in range(5):
   print("\nParent thread is executed")
#Statements will be mixed and printed.while child thread running a program.Main thread will be idle,so main thread will run a program
print("________________________________________________________________________")
#METHOD-3
#Using object
class gopal:
   def win(self):
      for i in range(6):
         print("\nChild thread is executed");
obj=gopal();
t=Thread(target=obj.win())
t.start()