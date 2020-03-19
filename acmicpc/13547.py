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

def mos(arr):#모스알고리즘 규칙
    s = arr[0]
    e = arr[1]
    ns = arr[0]
    ne = arr[1]    
    if s/k < ns/k or (s/k == ns/k and e < ne):
        return [s,e],[ns,ne]
    return [ns,ne],[s,e]

# qry = sorted(qry)
###정    렬###
# Q1먼저 처리하는 조건
# [s1/k] < [s2/k]
# [s1/k] = [s2/k] and e1 < e2
dq = []
print(qry)
print(sorted(qry,key=lambda x: [x[0]/k,-x[1]]))

# for i,qq in enumerate(qry):
#     if i+1 >= len(qry): break
#     qry[i],qry[i+1] = mos(qq,qry[i+1])
# print('==결과==\n','\n',qry)
##############
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