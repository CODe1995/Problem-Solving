import sys
input = sys.stdin.readline
N,K = map(int,input().split())
Warr,Varr = [0]*101,[0]*101
for i in range(N):Warr[i],Varr[i]=map(int,input().split())
dp = [[0]*100001 for _ in range(101)]
def calc(index,w):
    if dp[index][w]>0:return dp[index][w]
    if index==N:return 0
    a = 0
    if w+Warr[index]<=K:#무게가 안넘는다면
        a=Varr[index]+calc(index+1,w+Warr[index])#고르고
    b=calc(index+1,w)#안고르고
    dp[index][w]=max(a,b)
    return dp[index][w]
print(calc(0,0))