#write a program to check palindrome or not.
num =int(input("enter the number to check palindrom or not: "))
temp=num
rev=0
while num>0:
    dig=num%10
    rev =rev*10+dig
    num =num//10
if rev==temp:
    print("number is palindrome")
else:
    print("it is not a palindrome")