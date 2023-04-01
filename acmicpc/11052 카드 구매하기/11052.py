# https://kgh940525.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%B9%B4%EB%93%9C%EA%B5%AC%EB%A7%A4%ED%95%98%EA%B8%B0-11052-DP-%EC%B5%9C%EB%8C%93%EA%B0%92
N = int(input())
cards = [0] + list(map(int,input().split()))
dp = [0] * (N+1)

for i in range(1,N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + cards[j])
print(dp[N])



