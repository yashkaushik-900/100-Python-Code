#to calculate fibonacci series
def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n=int(input("enter the number"))
if n<=0:
    print("enter the positive number")
else:
    print("fibonacci")
    for i in range(n):
        print(fibonacci(i), end=' ')