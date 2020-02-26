def mod(a,b,c):
    if b==1: return a
    temp = pow(a,b//2,c)#두번째 b가 5여도 2가 나와서 홀수인 경우 따로 한번을 추가해줘야함
    if b%2:#홀수라면
        return (temp**2)%c*a%c
    else:#짝수라면
        return (temp**2)%c 

a,b,c = map(int, input().split())
print(mod(a%c,b,c))