from collections import Counter
import sys
###기본입력###
cnt = [0]*1000001
N = int(input())
k = N**0.5
Aarr = list(map(int,sys.stdin.readline().split()))
M = int(input())
qry=list()
for i in range(1,M+1):
    qry.append(list(map(int,sys.stdin.readline().split())))
##############
qry = sorted(qry)
###정    렬###
# Q1먼저 처리하는 조건
# [s1/k] < [s2/k]
# [s1/k] = [s2/k] and e1 < e2
dq = []
for i,[s,e] in enumerate(qry):
    if i+1 >= len(qry):        break
    ns = qry[i+1][0]
    ne = qry[i+1][1]
    #Q2 먼저 처리하는 조건
    print(qry)
    if s/k < ns/k:
        dq.append([s,e])
    elif s/k == ns/k and e < ne:
        dq.append([s,e])
    else:
        dq.append([ns,ne])
        qry[i],qry[i+1]=qry[i+1],qry[i]
##############

print('==결과==\n',dq,'\n',qry)
# for key,(left, right) in qry.items():
#     key = len(Counter(Aarr[left:right+1]))
#     print(key)
    # print(Counter(Aarr[left:right+1]),key) 

##############
# plo =0; phi =M
# tmp = A
# cnt=0
# cntr = Counter(tmp)
# for loopi,i,j in enumerate(qry):        
#     i=i-1;j=j-1    
#     if loopi==0:#반복문 처음이라면
#         cntr = Counter(tmp[i:j+1])        
#     else:
#         while i<plo:#현재가 이전보다 시작점이 낮다면 수를 더해야함            
#             # cntr|A[i]
#             print()
#         while i>plo:#현재가 이전보다 시작점이 높다면 수를 빼야함
#             # cntr.subtract(Counter([A[i],1])
#             print()
#         while j<phi:
#             # cntr.subtract(Counter([A[i],1])
#             print()
#         while j>phi:
#             # cntr|A[j]
#             print()
#     print(len(cntr))
    

#     plo=i;phi=j