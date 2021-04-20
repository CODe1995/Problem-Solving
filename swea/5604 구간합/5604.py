# N의 수를 9단위로 낮추어 연산하는 방식이다.


dp = dict()

def getV(x):#return v
    return 10**(len(str(x))-1)

def init():
    # 1~9까지의 합을 미리 계산해둔다.
    dp[0]=0
    for i in range(1,10):
        dp[i]=dp[i-1]+i
    #문제의 A,B 범위가 10^1 ~ 10^15이므로 1~15까지 생성해준다.
    #F(9) = 1*F(9) = 45
    #F(99) = 20*F(9) = 900
    #F(999) = 300*F(9)
    #F(9999) = 4000*F(9) ...
    for i in range(1,16):
        V = 10**i
        s = int('9'*i)
        dp[V-1] = int(str(i)+'0'*(i-1))*45  #F(9)=45


#########################################
#G(N,V) = N의 가장 큰 자릿수 * 해당 수가 몇갠지 + 아랫자리수도 비교
    # 1234라고 가정
        #N의 가장 큰 자릿수는 1
        #해당 수는 
#########################################
def G(N,V):
    if N<10:
        return dp[N]    #1부터 N까지의 합
    #N/V : N의 가장 큰 자릿수
        # 1234면 1, 9876이면 9
    # N%V+1 : 기준 값에서 N까지 등장하는 N/V의 횟수
    # 해당 수를 더해주기 위해서 사용된다.
    return N//V * (N%V+1) + F(N%V)

#########################################
#F(N) = part1 + part2
#part1: F(N의 바로 한단계 낮은 9단위의 수)
    # 예시1) 11의 경우 9
    # 예시2) 123의 경우 99
#part2: G(n) 현재 수에서 가장 큰 자리수의 합 
    # 예시) 25라면 21, 22, 23, 24, 25의 10의 자리수 2 + 2 + 2 + 2 + 2를 반환
#########################################
def F(N):
    if N in dp:
        return dp[N]
    V = getV(N)
    part1 = F(N-1 - N%V)
    part2 = G(N,V)
    result = part1+part2
    dp[N] = result
    return dp[N]

def calc(start,end):
    # start가 0인 경우 F(end)만 단독적으로 계산되어야 한다.
    return F(end) - F(0 if start==0 else start-1)

if __name__ == "__main__":
    init()
    TC = int(input())
    for tc in range(1,TC+1):
        start,end = map(int,input().split())
        print('#{} {}'.format(tc,int(calc(start,end))))