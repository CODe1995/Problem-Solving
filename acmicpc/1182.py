N,S = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
cnt = 0

for i in range(1,len(arr)):
    arr[i] += arr[i-1]

start = 0
end = 0

while start<=end and end<len(arr):
    prefix = arr[start] if start==end else arr[end]-arr[start] 
    if  prefix == S:
        cnt+=1
        start+=1
    elif prefix < S:
        end+=1
    else:
        start+=1
print(cnt)