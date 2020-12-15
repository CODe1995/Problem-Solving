dp=[0]*101
dp[1]=1
dp[2]=1
dp[3]=1
dp[4]=2
dp[5]=2
dp[6]=3
dp[7]=4
dp[8]=5
dp[9]=7
dp[10]=9
def calc(cs):
    if dp[cs]!=0:
        return dp[cs]
    if dp[cs-2]==0:
        dp[cs-2] = calc(cs-2)
    if dp[cs-3]==0:
        dp[cs-3] = calc(cs-3)
    dp[cs]=dp[cs-2]+dp[cs-3]
    return dp[cs]

T = int(input())
for i in range(T):
    cs = int(input())
    calc(cs)
    print(dp[cs])