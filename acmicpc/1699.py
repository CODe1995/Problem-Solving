#pypy3로 제출해야 시간초과 안뜸

N = int(input())
dp =[0]*100001  # 0은 아예 생각을 안하고 1부터 시작해서 +1
for i in range(1,N+1):
    dp[i]=i #일단 돌아가는건 dp에 저장
    for j in range(1,i):
        if (j**2)>i:
            break
        dp[i] = min(dp[i],dp[i-j**2]+1)
print(dp[N])