import sys
from math import gcd

def lcm(a,b):
    return a*b//gcd(a,b)

inp = sys.stdin.readline
Case = int(input())
datas = [list(map(int,input().split(' '))) for _ in range(Case)]
flag = True

# for M,N,x,y in datas:
    
