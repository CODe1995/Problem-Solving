import math
n = int(input())
dp = [0]*10001
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5
def isSquare(num):
    tmp = num**0.5    
    # print(num,tmp)
    return tmp*tmp==num
for i in range(5,10000):
    res = 1
    if i%2==0:res+=1#짝수라면 +1
    if isSquare(i):res+=1
    dp[i]=dp[i-1]+res
print(dp[n])