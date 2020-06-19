import sys
input = sys.stdin.readline
n,c = map(int,input().rstrip().split())
arr= []
arr2= []
for i in range(n):
    arr.append(int(input().rstrip()))
arr.sort()
for i in range(1,n):
    if i >= 1:
        arr2.append(arr[i]-arr[i-1])
print(arr,arr2)

