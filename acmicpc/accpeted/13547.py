# from collections import Counter
import sys

###기본입력###
cnt=[0]*1000001
cntnum = []
N = int(input())
k = N**0.5
Aarr = list(map(int,sys.stdin.readline().split()))
M = int(input())
qry=list()
for i in range(1,M+1):
    qry.append(list(map(int,sys.stdin.readline().split())))
##############
###정    렬###
# Q1먼저 처리하는 조건
# [s1/k] < [s2/k]
# [s1/k] = [s2/k] and e1 < e2

# qry = sorted(qry,key=lambda x: (x[0]//k,x[1]))

##############
def Qsub(number):
    cnt[number]-=1
    if cnt[number]==0:
        cntnum.remove(number)
def Qsum(number):
    cnt[number]+=1
    if cnt[number]==1:
        cntnum.append(number)

#################첫번째
for i in range(qry[0][0]-1,qry[0][1]):
    Qsum(Aarr[i])
print(len(cntnum))

###############
for i in range(1,M):    
    bs,be = qry[i-1][0]-1,qry[i-1][1]-1
    s,e=qry[i][0]-1,qry[i][1]-1
    while s>bs: Qsub(Aarr[bs]);bs+=1
    while s<bs: bs-=1;Qsum(Aarr[bs])
    while e>be: be+=1;Qsum(Aarr[be])
    while e<be: Qsub(Aarr[be]);be-=1
    print(len(cntnum))
###############
# for i in range(1,M):    
#     bs,be = qry[i-1][0]-1,qry[i-1][1]-1
#     s,e=qry[i][0]-1,qry[i][1]-1
#     if s>bs: cntqry.subtract(Counter(Aarr[bs:s])) 
#     if s<bs: cntqry=cntqry|Counter(Aarr[s:bs])
#     if e>be: cntqry=cntqry|Counter(Aarr[be+1:e+1])
#     if e<be: cntqry.subtract(Aarr[e+1:be+1])
#     print(len(cntqry&cntqry))