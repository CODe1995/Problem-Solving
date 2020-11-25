from math import gcd
def lcm(a,b):
    return a*b//gcd(a,b)
lists = input().split()
a = int(lists[0])
b = int(lists[1])
print(gcd(a,b))
print(lcm(a,b))