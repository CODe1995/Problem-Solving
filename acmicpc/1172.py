import sys
sys.setrecursionlimit(10000)    #재귀 한도 해제
n = int(input())
dp = [0]*1001
# 2 11 00 2
# 3 100 001 111 3
# 4 1111 0011 1001 1100 0000 5
# 5 11111 00111 10011 11001 11100 00001 00100 10000 8
def calc(n):
    if n==1: return 1
    if n==2: return 2
    if dp[n-1]:return dp[n-1]
    else: 
        dp[n-1] = calc(n-1) + calc(n-2)
        return dp[n-1]

print(calc(n)%10007)