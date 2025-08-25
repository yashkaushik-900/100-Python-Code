#to find natural numbers using recursion
def natural(num):
    if num<=1:
        return num
    else:
        return num + natural(num-1)
num=int(input("enter the number here: "))
print("The sum of natural numbers is:", natural(num))