def reverse(n):
    y=''

    for i in n:
        y=i+y
    return y

str=input("enter the strting  ")
result=reverse(str)
print(result)
