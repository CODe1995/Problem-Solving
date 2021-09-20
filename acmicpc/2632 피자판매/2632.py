import bisect
SIZE = int(input())
M,N = map(int,input().split())
Aarr = list(int(input()) for _ in range(M))
Barr = list(int(input()) for _ in range(N))
answer = 0
def makeSumArray(LIMIT, ARR):
    global SIZE
    tmpsum = [0]
    _max = False
    _maxsum = sum(ARR)
    for i in range(LIMIT):
        s=0
        for j in range(LIMIT):
            k = (i+j)%LIMIT
            s += ARR[k]
            if _max and s==_maxsum:
                break
            elif not _max and s==_maxsum:
                _max=True
            if s<=SIZE:
                tmpsum.append(s)
            else:
                break
    tmpsum.sort()
    return tmpsum

Asum = makeSumArray(M,Aarr)
Bsum = makeSumArray(N,Barr)

for i in range(len(Asum)):
    left = bisect.bisect_left(Bsum,SIZE-Asum[i])
    right = bisect.bisect_right(Bsum,SIZE-Asum[i])
    answer+=right-left
print(answer)