#find simple calculator 
n=float(input("enter the first number"))
m=float(input("enter the second number"))
print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")
choice=int(input("enter your choice"))
if choice==1:
    print("addition is",n+m)
elif choice==2:
    print("subtraction is",n-m)
elif choice==3:
    print("multiplication is",n*m)
elif choice==4:
    print("division is",n/m)
else:
    print("invalid input")