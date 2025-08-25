#program to chech if a number is positive , negative or zero
""" n=float(input("enter the number"))
if n>0:
    print("number is positive",n)
elif n<0:
    print("number is negative",n)
else:
    print("number is zero",n) """

#program to check number is odd or even
""" i=int(input("enter the number"))
if i%2==0:
    print("number is even ",i)
else:
    print("number is odd",i) """

#check prgram number is leap year or not
""" num =int(input("enter the number of year"))
if (num%400==0) and (num%100==0) :
    print("number is leap year",num)
elif (num%4==0) and (num%100 !=0) :
    print("number is leap year",num)
else:
    print("number is not leap year--------------------------------------------------") """

#check program 3 number is greatest or not
""" n=int(input("enter the number 1 "))
m=int(input("enter the number 2 "))
p=int(input("enter the number 3 "))
if n>m and n>p:
    print(n,"number is greatest")
elif m>n and m>p:
    print(m,"number is greatest")
else:
    print(p,"is greatest number") """

#python program to check number is prime number or not
""" n= int(input("enter the number of check prime or not"))
if n==1:
    print(n,"is a prime number")
for i in range(2,n):
    if n%i==0:
        print(n, "is a not prime number")
        break
    else:
        print(n,"is a prime number")
        break """

#python proram to check number prime number in range interval
""" lower =int(input("enter the lower number"))
upper =int(input("enter the upper number"))
for num in range(lower,upper+1):
    if num==1:
        print(num,"prime number")
    elif num>1:
        for i in range(2,num):
            if num%i==0:
                print(num,"not prime number")
                break
        else:
            print(num) """
