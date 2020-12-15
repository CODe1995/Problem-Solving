t=0
data = []
for i in range(4):
    a, b= map(int,input().split())
    t-=a; t+=b
    data.append(t)
print(sorted(data)[3])
