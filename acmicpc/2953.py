data = []
rank = 1
for i in range(5):
    t=list(map(int,input().split()))
    data.append(sum(t))
    if data[rank-1] < data[i]:
        rank = i+1
print(rank,sorted(data)[4])