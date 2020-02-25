import sys
inp = sys.stdin.readline
K,N = map(int,input().split())
data = []
for i in range(K):
    data.append(int(inp().strip()))
data = sorted(data,reverse=True)
right = data[0]
left = 0
result = 0
while left<=right:
    mid = (left+right)//2    
    #갯수가 나오는지 체크
    cnt = 0
    for i in data:
        cnt += i//mid
        if(cnt>=N and mid>result):
            result = mid
            break
    if cnt<N:
        right = mid-1
    else:
        left = mid+1
print(result)
        
