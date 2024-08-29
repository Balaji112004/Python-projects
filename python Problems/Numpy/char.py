import numpy as np;
ch=np.array(['Balaji','Ajith'])
print(ch)
#Note
#We use range in list
#But in numpy,We use arrange
l=range(6)
print(l)

n=np.arange(6)
print(n)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
z=np.zeros([3,4])#To create 0 array
print(z)

o=np.ones([4,5])#To create 1 array
print(o)
print("______________________________________________________________________")
print("Concatenation example")
print(np.char.add(['Hello','Hi'],[' World',' Hello']))
print("Multiplying the char")
print(np.char.multiply("Hello ",6))
print("Center the string:",np.char.center("Balaji",20,fillchar='*'))