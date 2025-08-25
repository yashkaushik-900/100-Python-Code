#write a program to calculate factorial numbers.
""" num=int(input("enter the number: "))
fact=1
if num<0:
    print("factorial does not exist")
if num==0:
    print(num)
if num>0:
    for i in range(1,num+1):
        fact=fact*i
print("the factorial number is ",fact) """
#using recursion

def fact(n):
    if n==0:
        return 1
    else:
        return ((n)*fact(n-1))
na=int(input("enter the number: "))
result=fact(na)
print("result of factorial is :",result)