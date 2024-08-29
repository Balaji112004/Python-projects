class car():

    def __init__(self,year,speed):
        self.year=year;
        self.speed=speed;

    def speed(self):
        print("Maximum speed:",self.speed)

class sedan(car):

      def sedanfun(self):
          print(157)
      def speed(self):
          print("It is function of sedan")

Honda=car(2018,260)
Audi=sedan(2019,312)

car.speed(Honda);
sedan.speed(Audi)#Here,both class car and sedan have same function name;