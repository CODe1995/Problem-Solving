import sys
k,n=map(int,input().split())
cables = [int(sys.stdin.readline()) for _ in range(k)]
# cables = sorted(cables,reverse=True)
# print(cables)
right = max(cables)
left = 0
while left<=right:    
    cnt=0    
    mid = (right+left)//2
    if mid ==0:#0으로 나누는 모듈러 에러 방지
        break
    for i in cables:
        cnt += i//mid        
    if cnt >= n:#갯수를 줄여야함 = 길이를 늘려야함
        left = mid + 1
    else:
        right = mid - 1
print(right)