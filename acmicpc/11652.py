n = int(input())
arr = {}
for i in range(n):
    tmp = int(input())
    if tmp in arr:
        arr[tmp]+=1
    else:
        arr[tmp]=1
arr = sorted(arr.items())
print(arr[0][0])