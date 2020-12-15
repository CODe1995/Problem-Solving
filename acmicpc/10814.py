T= int(input())
data =[]
for i in range(T):
    data.append(list(map(str,input().split())))
    data[i][0]=int(data[i][0])
for i in sorted(data, key=lambda age:age[0]):
    print(i[0],i[1])