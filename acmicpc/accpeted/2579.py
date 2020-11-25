import sys
input = sys.stdin.readline
N = int(input().rstrip())
dp = []
scores = []
for i in range(N):
    scores.append(int(input().rstrip()))
if N>2:
    dp.append(scores[0])
    dp.append(dp[0]+scores[1])
    dp.append(max(dp[0]+scores[2],scores[1]+scores[2]))
    for i in range(3,N):
        dp.append(max(dp[i-2]+scores[i],dp[i-3]+scores[i-1]+scores[i]))
    print(dp.pop())
else:
    print(sum(scores))