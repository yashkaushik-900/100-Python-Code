#program add two number 
# solutin 1 pre-defined variables
'''n = 21
m = 54
print("the sum of given two number is ",n+m) '''
# solution 2 user defined 
'''n = float(input("enter the first number"))
m = float(input("enter the second number"))
sum = m+n
print("sum of two number is ", (m+n)) '''
#hellod world to print python program
#print("hello world") 

#python program to find the square root
#solution 1 using exponentiation
#n = 64
'''m = int(input("enter the number here..."))
sr =n**(1/2)
print("the square root of given number is ....",sr)'''

""" import math
num =int(input("enter the number here.."))
sr =math.sqrt(num)
print("the square of given number is",sr) """

#python program to find the area of triangle
""" base = int(input("enter the base of triangle is ..."))
height = int(input("enter the height of triangle is ..."))
tri = ((1/2)*base *height)
print("Area of triangle is ...",tri) """

#python program to find the quadratic equation
""" import cmath
a = int(input("enter the number but (a!=0)"))
b =int(input("enter the number "))
c =int(input("enter the number..."))
#formula of discriminant
d = (b**2) - (4*a*c)
#formula of quadratic equation
root1 = (-b + cmath.sqrt(d)) / (2 *d)
root2 = (-b - cmath.sqrt(d)) / (2 *d)
print("the roots of quadratic equation are", root1, "and",root2) """

#python program to swap two variables
""" a= int(input("enter the first number here..."))
b=int(input("enter the second number here..."))
#swapping using third variable
temp=a
a=b
b=temp
print("swapping of two variables",(a,b)) """
#swapping second method
""" a=3
b=4
a,b=b,a
print("swapping two variables",(a,b)) """

#python program to generated a random number
""" import random
num = random.randint(0,10)
print(num) """

#python program convert kilometers to miles
""" num =float(input("enter the number..."))
miles = (0.624371)*num
print("km in miles will be",miles) """

#python program convert celsius to fahrenheit
""" cel =float(input("enter the temperature of celcius ..."))
far = ((9/5)*cel)+32
print(far,"temperature is ..") """