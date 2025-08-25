#write a program to find a sum all the even numbers up to 50.
""" sum=0
for i in range (1,51):
    if i%2==0:
        sum+=i
print(sum,"sum of all even numbers") """

#write a program to write first 20 even numbers and their
#squared numbers
""" for i in range (1,21):
    print(i,i**2 )"""
#write a program to find sum of 10 digit odd numbers using while loop.
""" sum=0
n=0
while n<=20:
    if n%2!=0:
        sum+=n
    n+=1
print(sum,"result of sum 10 odd digits numbers")
 """
#write a program to check if a number is divisible by 8 and 12 , upto 100 numbers.
""" for i in range (1,101):
    if i%8==0 and i%12==0:
        print(i) """
#write a program to create a billing in supermarketing.
""" while True:
    Name =input("enter the name ")
    total=0
    while True:
        quantity=float(input("enter the quantity of product"))
        amount=float(input("enter the amount"))
        total+=amount*quantity
        repeat =input("do you want to add more items: y/n")
        if repeat =="y" or repeat=="n":
            break
    print("--------------------------------------------------")
    print("name", Name)
    print("amount to be paid", total)
    print("------------------------------------------")
    print("happy shopping *******************************************************")
    repeat1=input("do you want to next customer ?y/n")
    if repeat1=="y" or repeat1=="n":
        break """