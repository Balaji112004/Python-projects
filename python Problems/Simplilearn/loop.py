x=[[1,2,3,4],['a','b','c','d']]
for i in x:
    for j in i:
        print(j,end='')
    print()
# patterns
num=int(input("Enter the number:"))
for i in range(1,num+1):
    for j in range(1,i):
        print(j,end='')
    print()

#
r=int(input("Enter the row:"))
c=int(input("Enter the column:"))
val=[]
X=[]
for i in range(0,r):
    for j in range(0,c):
        val.insert(j,int(input("Enter %d * %d element:" %(i,j))))
    X.insert(i,val)

for i in range(0,r):
    for j in range(0,c):
        print('[ %d ]' %X[i][j],end='')
    print()

n=5678
ce=n%10;
print(ce);