def func(*args):
    for i in args:
        print(i);
func(1,2,3,4,'balaji')
print("------------------------------------")
def func2(**kwargs):
    for j in kwargs.items():
        print(j);

func2(a=10,b=20,c=25)