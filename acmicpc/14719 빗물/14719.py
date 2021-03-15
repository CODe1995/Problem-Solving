W,H = map(int,input().split())
arr = list(map(int,input().split()))
totalMax = 0
tidx = -1
for i in range(len(arr)):
    if totalMax < arr[i]:#최고 높이 갱신
        totalMax = arr[i]
        tidx = i#위치 기억
height = 0
answer = 0
for i in range(tidx):
    if height!=0 and height>arr[i]:
        answer+=height-arr[i]
    if height<arr[i]:
        height=arr[i]
height=0
for i in range(len(arr)-1,tidx,-1):
    if height!=0 and height>arr[i]:
        answer+=height-arr[i]
    if height<arr[i]:
        height=arr[i]
print(answer)