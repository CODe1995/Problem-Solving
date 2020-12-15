cnt = 0
ans = list()
def hanoi(n,F,M,T):
    global cnt
    if n==1:
        ans.append([F,T])
        # print('n: %d, F: %d, M: %d, T: %d'%(n ,F ,M ,T))
    else:
        hanoi(n-1,F,T,M)
        ans.append([F,T]) 
        # print('n: %d, F: %d, M: %d, T: %d'%(n ,F ,M ,T))
        hanoi(n-1,M,F,T)
    cnt+=1

hanoi(int(input()),1,2,3)
print(cnt)
for pos in ans:print(pos[0],pos[1])
