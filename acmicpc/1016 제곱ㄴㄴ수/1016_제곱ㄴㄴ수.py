import sys
input = sys.stdin.readline
# MIN,MAX = map(int,input().split())
def solution(MIN,MAX):
    answer = MAX-MIN+1
    check = [False]*(MAX-MIN+1)
    i=2
    while i*i <= MAX:
        square_number = i*i #제곱수
        # remain
        # 제곱수가 딱 나누어 떨어지면 상관없지만 그게 아니라면 소수점이 버림 처리 된다.
        # 그래서 remain으로 그 값을 보정해준다.
        remain = 0 if MIN%square_number==0 else 1
        j = MIN//square_number + remain #제곱수로 나눈 몫 => 배수
        while square_number*j <= MAX:   #제곱수의 j배 (에라토스테네스의 체)
            if not check[square_number*j-MIN]:
                check[square_number*j-MIN]=True
                answer-=1
            j+=1#배수 점점 증가
        i+=1        
    print(answer)
a,b = map(int,input().split())
solution(a,b)
# solution(1000000,2000000)
# solution(1,10)