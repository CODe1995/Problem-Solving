k,n=map(int,input().split())
cables = []
for _ in range(k):
    cables.append(int(input()))
cables = sorted(cables,reverse=True)
# print(cables)
right = cables[0]
left = 0
while left<=right:    
    cnt=0
    mid = (right+left)//2
    for i in cables:
        cnt += i//mid
    if cnt >= n:#갯수를 줄여야함 = 길이를 늘려야함
        left = mid + 1
    else:
        right = mid - 1
print(right)