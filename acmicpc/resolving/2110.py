import sys
input = sys.stdin.readline
n,c = map(int,input().rstrip().split())

arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort()

spnt = 1    #가능한 최소 거리
epnt = arr[-1]-arr[0]   #가능한 최대 거리
answer = 0 #정답

while spnt<=epnt:
    mid = (spnt+epnt)//2    #목표로 두는 거리
    crit = arr[0]   #기준점
    distance = 0 #기준점으로부터의 거리
    cnt=1   #공유기 하나는 이미 설치했으므로 1부터 카운트
    # 0번은 설치를 했다고 가정했으므로    
    # idx 1부터 반복문 시작한다.
    for i in range(1,n):
        #현재 기준으로부터 거리를 측정
        distance = arr[i]-crit
        #현재 거리가 mid보다 작거나 같으면
        #설치를 할 수 있다.
        if mid<=distance:
            cnt+=1
            crit = arr[i]#기준점 갱신
    
    if cnt>=c:#설치갯수가 많거나 같으면
        #거리를 늘려서 시도해볼만하다.
        #즉 mid 크기를 키워야한다.
        spnt+=1
        answer = mid
    elif cnt<c:#설치 공유기 갯수가 적으면
        #mid 크기를 줄여야한다.(거리를 좁히자)
        epnt-=1
print(answer)