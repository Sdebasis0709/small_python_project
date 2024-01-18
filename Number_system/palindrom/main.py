def palindrom(num):
    temp=num
    result=0
    while num>0:
        dgt=num%10
        result=result*10+dgt
        num=num//10
    if result==temp:
        return "palindrom number"
    else:
        return "not a palindrom number"
n=int(input("enter the number:  "))
result=palindrom(n)
print(result)
