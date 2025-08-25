#python program to convert decimal to binary
dec=int(input("enter a decimal number"))
print("conversion of decimal number ", dec,"is")
#using bin function
print(bin(dec),"in binary")
print(oct(dec),"in octal")
print(hex(dec),"in hexadecimal")
#using recursion
def convert(num):
    if num>1:
        convert(num//2)
    print(num%2, end='')