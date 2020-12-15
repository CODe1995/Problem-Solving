N=int(input())
data=list(map(int,input().split()))
num = set(data)
for i in sorted(num):
    print(i,end=' ')