n = int(input())
data = list([input()for _ in range(n)])
data = set(data)
data = sorted(data,key=lambda x: (len(x),x[0],x[1:]))
for i in data:
    print(i)