from math import gcd    #최대공약수
def lcm(a,b):
    pt = gcd(a,b)    
    return pt*a//pt*b//pt
T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    print(lcm(A,B))