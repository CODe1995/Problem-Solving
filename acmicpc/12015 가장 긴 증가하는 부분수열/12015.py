import bisect
# bisect_left를 하는 이유?
# 
N = int(input())
arr = list(map(int,input().split()))
dp = list()

for i in range(N):
    k = bisect.bisect_left(dp,arr[i])#자신이 들어갈 위치 기억
    if len(dp)<=k:#k=len(dp) : 들어갈 위치가 가장 우측 = 가장 큰 수
        dp.append(arr[i])
    else:
        dp[k] = arr[i]#자신보다 큰 수 중 최솟값과 대체
print(len(dp))