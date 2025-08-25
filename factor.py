#factors of a number finding
num=int(input("enter the number for finding factors"))
for i in range(1,num+1):
    if num%i==0:
        print("factors is ",i)