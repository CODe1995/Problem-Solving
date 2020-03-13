from collections import Counter

###기본입력###
N = int(input())
A = list(map(int,input().split()))
M = int(input())
qry=list()
for i in range(1,M+1):
    cnt = 0
    qry.append(list(map(int,input().split())))
##############

plo =0; phi =M
tmp = A
cnt=0
cntr = Counter(tmp)
for loopi,i,j in enumerate(qry):        
    i=i-1;j=j-1    
    if loopi==0:#반복문 처음이라면
        cntr = Counter(tmp[i:j+1])        
    else:
        while i<plo:#현재가 이전보다 시작점이 낮다면 수를 더해야함            
            # cntr|A[i]
            print()
        while i>plo:#현재가 이전보다 시작점이 높다면 수를 빼야함
            # cntr.subtract(Counter([A[i],1])
            print()
        while j<phi:
            # cntr.subtract(Counter([A[i],1])
            print()
        while j>phi:
            # cntr|A[j]
            print()
    print(len(cntr))
    

    plo=i;phi=j

