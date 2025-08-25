#write a program to check prime or not.
num =int(input("enter the number check prime or not: "))
if num==1:
    print("it is not a prime number")
else:
    for i in range(2,num):
        if num%2==0:
            print("it is not a prime number: ")
            break
        else:
            print("it is a prime numbers:")
            break