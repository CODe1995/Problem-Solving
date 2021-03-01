import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().strip().split())) for _ in range(N)]
arr.append(arr[0])
xsum = 0
ysum = 0
for i in range(N):
    ysum+=arr[i][1]*arr[i+1][0]
    xsum+=arr[i][0]*arr[i+1][1]
print("%.1f"%((abs(ysum-xsum))/2))