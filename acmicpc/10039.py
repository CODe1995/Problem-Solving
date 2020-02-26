data = []
for i in range(5):
    t = int(input())
    if t<40:data.append(40)
    else:data.append(t)
print(sum(data)//5)
