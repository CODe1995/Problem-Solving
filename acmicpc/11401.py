#math.factorial은 시간초과, 그래서 factorial을 dp로 풀자
#dp문제 + 페르마의소정리, 확장유클리드호제법으로 풀어야한다
#페르마의소정리를 사용했고, dp를 활용해서 전처리함
#https://www.acmicpc.net/board/view/15795
p = 1000000007 #소수 
dp=[0]*4000001
dp[0]=1
dp[1]=1
dp[2]=2
dp[3]=6

# def fact(num):
#     if dp[num]!=0:
#         return dp[num]
#     #p를 mod해주는 이유
#     dp[num]=fact(num-1)*num
#     return dp[num]

def daca(x,y):
    while y>0:
        ret = 1
        if y%2==1:
            ret*=x
            ret%=p
        x=(x*x)%p
        y=y//2
    return ret

#미리 전처리 시켜두고 어떤 값이 들어와도 처리가 가능하게 만듦
# fact(4000000)#팩토리얼 전처리
for i in range(4,4000001):
    dp[i] = (dp[i-1]*i)%p

inv = [0]*4000001
inv[4000000]=daca(dp[4000000],p-2)
for i in range(3999999,0,-1):#역순으로
    inv[i] = (inv[i+1]*(i+1))%p


n,k=map(int,input().split())
if n==k:#n과k가 같으면 1임
    print(1)
else:
    print(dp[n]%p * inv[n]%p)