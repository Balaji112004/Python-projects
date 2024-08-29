import pandas as pd;
print(pd.__version__)
arr1=[2,4,6,8,10]
arr2=[1,3,5,7,9]
s1=pd.Series(arr1)
s2=pd.Series(arr2)
print(s1)
print(s2)
s3=s1._append(s2)
print(s3)