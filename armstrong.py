""" n=int(input("enter the number: "))
order=len(str(n))
sum=0
temp=n
while temp>0:
    digit=temp%10
    cube=digit**order
    sum=sum+cube
    temp//=10
if sum==n:
    print("it is armstrong number",n)
else:
    print("it is not armstrong number") """

#interval based armstrong numbers.
lower=int(input("enter the lower number"))
upper=int(input("enter the upper number"))
for n in range(lower,upper+1):
    order=len(str(n))
    temp=n
    sum=0
    while temp>0:
        digit=temp%10
        cube=digit**order
        sum=sum+cube
        temp//=10
    if sum==n:
        print("it is armstrong number",n)
    """ else:
        print("it is not armstrong number")
        break """