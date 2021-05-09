import math
n = int(input())
dp = [0]*10001
divisor = [False]*10001
dp[1] = 1
divisor[1] = True
dp[2] = 2
def check(num):
    for i in range(math.sqrt(num)):
        if num%i==0:
            if not divisor[num/i]:
                divisor[n]

for i in range(5,10000):
    res = 1
    if i%2==0:res+=1#짝수라면 +1
    if isSquare(i):res+=1
    dp[i]=dp[i-1]+res
print(dp[n])