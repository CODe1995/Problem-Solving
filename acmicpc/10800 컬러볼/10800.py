import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
arr = [[i]+list(map(int,input().split())) for i in range(N)]
ans = [0]*200002
colorSum = [0]*200002
total = 0
arr = sorted(arr,key = lambda x:x[2])
i=0
while i<N:
    # print('start',i)
    pos = i
    while pos<N and arr[i][2]==arr[pos][2]:
        pos+=1
    
    for j in range(i,pos):
        ans[arr[j][0]] = total - colorSum[arr[j][1]]

    for j in range(i,pos):
        total += arr[j][2]
        colorSum[arr[j][1]] += arr[j][2]
    
    i = pos-1
    i+=1
    # print('last',i)

for a in range(N):
    print(str(ans[a])+"\n")