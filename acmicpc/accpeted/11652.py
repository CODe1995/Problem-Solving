n = int(input())
arr = {}
for i in range(n):
    tmp = int(input())
    if tmp in arr:
        arr[tmp]+=1
    else:
        arr[tmp]=1
arr = sorted(arr.items(),key=lambda x:(-x[1],x[0]))
print(arr[0][0])