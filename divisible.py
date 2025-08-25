#using for loop
""" print("divisible by 13")
for i in range(1,100):
    if i %13==0:
        print(i) """
#using lambda function
print("divisible by 13 using lambda")
result= list(filter(lambda x: x % 13 == 0, range(1, 100)))
print(result)