n = int(input())
cnt=0
data = list(map(int,input().split()))
for i in data:
    if i==n:
        cnt+=1
print(cnt)