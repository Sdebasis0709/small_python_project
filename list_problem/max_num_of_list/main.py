l=[]
n=int(input("Enter how many integers you want to add in list:   "))
for i in range(1,n+1):
    ele=int(input("Enter your Element:  "))
    l.append(ele)
x=l[0]
for y in l:
     if x < y:
        x= y
print("max ele of list is : " ,x)