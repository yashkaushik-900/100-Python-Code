#write a program to check if a number is positive.
'''num = int(input("enter the number to check positive or not:"))
if num>0 : print("number is positive")
elif num<0: print("number is negative")
else :
    print("number are equal to each other")'''
#write a program to check whether a number is odd or even.
'''n = int(input("enter the number"))
if n%2==0:
    print("number is even")
else:
    print("number is odd")'''
#write a program to create area calculator.
'''print("""
press 1 to get the area of square
press 2 to get the area of rectangle
press 3 to get the area of circle
press 4 to get the area of triangle""")
choice = int(input("enter the number between 1 to 4"))
if choice ==1:
    side = int(input("enter the lenght of side of square"))
    area = side**2
    print(area,"is the square of area")
elif choice ==2:
    length = int(input("enter the length of rectangle"))
    breadth = int(input("enter the breadth of rectangle"))
    rect = length*breadth
    print("result the area of rectangle is", rect)
elif choice ==3:
    rad = float(input("enter the radius of circle"))
    area =((3.14)*rad**2)
    print("result the area of circle is", area)
elif choice ==4:
    base = int(input("enter the base of triangle"))
    height = int(input("enter the height of triangle"))
    ar = ((1/2)*base*height)
    print("result the area of tra",ar)
else :
    print("invalid statement")
'''
#write a program chech whether the passed letter is a vowel or not.
"""letter = input("enter the letter here...")
if (letter in 'aeiou')or (letter in "AEIOU"):
    print("it is vowel letter")
else :
    print("it is not vowel letter...")"""

#write a program to check if a number is a single digit number, 2-digit number and so on.., up to 5 digits.
"""num = int(input("enter the digit "))
if num >=0 and num< 9:
    print("it is single digit number")
elif num> 10 and num<=99:
    print("it is a double digit number")
elif num> 100 and num<= 999:
    print("it is triple digit number")
elif num>1000 and num<= 9999:
    print(" it is quartz digit number")
elif num>1000 and num<=99999:
    print("it is 5th digit number")
else :
    print(" more than 5 digit number")"""