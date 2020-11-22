import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int,input().rstrip().split()))
arr.sort()
nL=0
nR=0
num = 1000000001    #최대값
for i in range(N):
    for j in range(i+1,N):
        if num>abs(arr[i]+arr[j]):
            num=abs(arr[i]+arr[j])
            nL = arr[i]
            nR = arr[j]
            if num==0:
                break      
for n in sorted([nL,nR]):
    print(n,end=' ')