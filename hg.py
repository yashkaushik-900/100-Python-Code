#findhcf and gcd using functions
def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf
print("HCF is", hcf(12, 18))
""" def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x """