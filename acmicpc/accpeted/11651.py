import sys
T = int(input())
inp = sys.stdin.readline
data= []
for i in range(T):
    data.append(list(map(int,inp().split())))
data = sorted(data,key=lambda y: y[1])
for i in range(T):
    for j in range(i+1,T):
        if data[i][1] == data[j][1] and data[i][0] > data[j][0]:
            data[i],data[j]=data[j],data[i]
        elif data[i][1] != data[j][1]:
            break

for i in range(T):
    print(data[i][0],data[i][1])