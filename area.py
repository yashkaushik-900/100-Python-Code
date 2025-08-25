#write a program to calculate the area of calculator.

print("@@@@@@@@@@@@@@@@@@@@@Area calculator $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
while True:
    print("""Press 1 to get the area of square" \
    Press 2 to get the area of rectangle:
    press 3 to get the area of circle
    press 4 to get the area of triangle:
    """)
    choice= int(input("enter the number between 1-4: "))
    if choice==1:
        while True:
            num =float(input("enter the number for square: "))
            choice =num*num
            print(choice,"result of square is :")
            repeat=input("do you want to repeat this line yes/no ")
            if repeat=="no":
                break
    if choice==2:
        while True:
            l=float(input("enter the length of rectangle: "))
            m=float(input("enter the breadth of rectangle:"))
            choice=l*m
            print(choice,"result of rectangle: ")
            repeat=input("do you want to repeat this line yes/no ")
            if repeat=="no":
                break
    if choice==3:
        while True:
            rad=float(input("enter number of circle :"))
            choice=(3.14)*rad**2
            print(choice,"result of circle")
            repeat=input("do you want to repeat this line yes/no ")
            if repeat=="no":
                break
    if choice==4:
        while True:
            b=float(input("enter the breadth:"))
            h=float(input("enter the height"))
            choice=(1/2)*b*h
            print(choice,"result of circle")
            repeat=input("do you want to repeat this line yes/no ")
            if repeat=="no":
                break
    repeat1 =input("do you want to repea this line:")
    if repeat1=="no":
        break
    