N = int(input())
weightList = list(map(int,input().split()))
weightList.sort()
sumWeight = 0
for i in range(N):
    w = weightList[i]
    if sumWeight+1 < w:
        break
    sumWeight += w
print(sumWeight+1)