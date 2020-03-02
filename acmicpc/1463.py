# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
# 연산을 사용하는 횟수의 최솟값을 출력하시오.
def calc(nlist):
    arr=[]
    for i in nlist:
        arr.append(i-1)
        if i%3==0:arr.append(i/3) 
        if i%2==0:arr.append(i/2) 
    arr =list(set(arr))
    # print(arr)
    return arr

N=int(input())
cnt=0
rs=[N]
while N>1:#1은 안받아도 됌
    tmp=rs
    rs = calc(tmp)
    cnt+=1
    if min(rs)==1:#1이 됐을때 탈출
        break
print(cnt)