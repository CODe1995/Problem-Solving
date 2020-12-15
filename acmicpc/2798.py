n,m=map(int,input().split())
data = sorted(list(map(int,input().split())))
tmp=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            sdata=data[i]+data[j]+data[k]
            if sdata<=m and tmp<sdata:
                tmp=sdata
print(tmp)