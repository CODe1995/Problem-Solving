import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int,input().rstrip().split()))
arr.sort()
nL,nR=0,0
num = 1000000001    #최대값
left,right=0,len(arr)-1
while left!=right:
    tP = abs(arr[left]+arr[right])
    if num>tP:
        num=tP
        nL = arr[left]
        nR = arr[right]
        if num==0:
            break
    if 0<tP:#합을 낮춰야함
        right-=1    #합이 작아짐
    else:
        left+=1 #합이 커짐    
      
for n in sorted([nL,nR]):
    print(n,end=' ')