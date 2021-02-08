from collections import deque
import sys
input = sys.stdin.readline
MIN = -10e9
N = int(input())
M = int(input())
arr = [MIN]*1000001
dq = deque()
xs = list(map(int,input().split()))
for x in xs:
    arr[x] = 0
    dq.append(x)
maxnum = 0
while dq:
    x = dq.popleft()
    for i in range(20):
        nx = x^ (1<<i)
        if nx>N or arr[nx]!= -10e9:
            continue
        dq.append(nx)
        arr[nx]=arr[x]+1
        maxnum = max(arr[nx],maxnum)
print(maxnum)