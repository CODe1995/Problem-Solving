od = []
for i in range(7):
    t = int(input())
    if t%2 !=0:
        od.append(t)
if len(od)==0:
    print(-1)
else:
    print(sum(od))
    print(sorted(od)[0])

