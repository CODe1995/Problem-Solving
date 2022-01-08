N = int(input())
weightList = list(map(int,input().split()))
possibleWeight = dict()
answer = 1000000*1000+1
for i in range(N):
    w = weightList[i]
    keys = list(possibleWeight.keys())
    for pw in keys:
        nextWeight = pw+w
        if nextWeight not in possibleWeight:
            possibleWeight[nextWeight] = 1
        nextWeight = pw-w
        if nextWeight <= 0:
            continue        
        if nextWeight not in possibleWeight:
            possibleWeight[nextWeight] = 1
    if w not in possibleWeight:
        possibleWeight[w] = 1
for i in range(1,1000000*1000+1):
    if i not in possibleWeight:
        print(i)
        break