T = int(input())
data =[]
for i in range(T):
    data.append(list(map(int,input().split())))

for i in data:
    value = 1
    for j in data:
        if i[0]<j[0] and i[1]<j[1]:
            value+=1
    print(value,end=' ')