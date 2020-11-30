import sys
input = sys.stdin.readline
n,h = map(int,input().rstrip().split())
arr_ground = []
arr_sky = []
for i in range(n):
    if i%2!=0:
        arr_sky.append(int(input()))
    else:
        arr_ground.append(int(input()))
answer = 1#최소 구간 갯수
minBreak = n#최소 파괴 횟수(초기값은 최대로)

arr_sky.sort()
arr_ground.sort()
#첫번째건 땅

def BS(arr,height):#binary search 함수
    left = 0
    right = len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid]>=height:
            right = mid-1
        else:
            left = mid+1
    return len(arr)-left

for height in range(1,h+1):#i는 높이
    sky_cnt = BS(arr_sky,h-height+1)
    ground_cnt = BS(arr_ground,height)
    sg_cnt = sky_cnt + ground_cnt

    if minBreak>sg_cnt:
        minBreak = sg_cnt
        answer=1
    elif minBreak==sg_cnt:
        answer+=1
print(minBreak,answer)