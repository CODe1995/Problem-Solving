import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().strip().split())) for _ in range(N)]

days = [0]*367

for a in arr:
    for i in range(a[0],a[1]+1):
        days[i]+=1

width=0
height=0
answer=0
for i in range(367):
    if days[i]>0:
        width+=1
        height=max(days[i],height)
    elif width>0 and days[i]==0:
        answer+=width*height
        width=0
        height=0
print(answer)