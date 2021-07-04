n = int(input())
arr = list(map(int,input().split()))
d = dict()
depth = 0

for i in sorted(arr):
    if i in d:continue
    d[i] = depth    
    depth+=1

for a in arr:
    print(d[a],end=' ')