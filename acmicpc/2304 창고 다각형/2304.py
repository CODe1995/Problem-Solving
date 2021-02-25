N = int(input())
arr = list()
for _ in range(N):
    arr.append(list(map(int,input().split())))
arr.sort()
pos = 1
# print(pos,arr)
while pos<len(arr)-1:
    if arr[pos][1]<arr[pos-1][1]:
        arr.pop(pos)
        print(pos,arr)
    else:pos+=1
answer =0
for i in range(len(arr)-1):
    if i==len(arr)-2:#뒤에서 두번째
        if arr[i][1]<arr[i+1][1]:
            answer+=(arr[i+1][0]-arr[i][0]) * arr[i][1] + arr[i+1][1]
        else:
            answer+=arr[i][1] + (arr[i+1][0]-arr[i][0])*arr[i+1][1]
    else:
        answer+=(arr[i+1][0]-arr[i][0]) * arr[i][1]

print(answer)