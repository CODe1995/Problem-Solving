import sys
input = sys.stdin.readline
N = int(input().rstrip())
dp = []
dp.append(1)
dp.append(2)
for i in range(3,N+1):    
    num = str(bin(i))
    if num[2]=='1' and '11' not in num:
        dp.append(dp[i-2]+1)
    else:
        dp.append(dp[i-2])
print(dp[N-1])
    