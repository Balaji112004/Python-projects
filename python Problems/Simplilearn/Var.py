x,y,z="Bananas","Apple","Orange";
print(x)
print(y)
print(z)
print("2 Dimensional Array")
row=int(input("Enter the size of row:"))
col=int(input("Enter the size of column:"))

arr=[]
for i in range(row):
    row=[]
    for j in range(col):
        ele=int(input("Enter the element:"))
        row.append(ele)
    arr.append(row)

