# Combination 문제다..
def combination(n,r):
    denominator=factorial(r)*factorial(n-r)
    molecule=factorial(n)
    return molecule//denominator
def factorial(n):
    if n>1:    
        return n * factorial(n-1)
    return 1
T = int(input())
for i in range(T):
    M,N = map(int,input().split())
    print(combination(N,M))