def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n==2:
        return 2
    else:
       return n*fact(n-1)
num=int(input("enter the number:   "))
factorial=fact(num)
print(factorial)