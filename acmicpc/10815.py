import sys
input = sys.stdin.readline
numarr = dict()
ans=list()
n = int(input().rstrip())
arr1 = list(map(int,input().rstrip().split()))
m = int(input().rstrip())
arr2 = list(map(int,input().rstrip().split()))
for i in arr1:    
    numarr[i] = 1
for j in arr2:
    try:
        if numarr[j]==1:
            ans.append(1)
    except:
        ans.append(0)
for i in ans:
    print(i,end=' ')