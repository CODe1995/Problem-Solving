import math
N,K = map(int,input().split())
num = list(map(int,input().split()))
minidx = num.index(1)
cnt = 0
if N<=K or (minidx<=K or minidx>= N-K):
    #한방에 되는경우
    cnt= 1 + math.ceil((N-K)/(K-1))
else:    
    pos = minidx%(K-1)
    cnt += math.ceil(len(num[:minidx-pos+1])/(K-1))
    cnt += math.ceil(len(num[minidx+K-pos:])/(K-1))
print(cnt)
    
    