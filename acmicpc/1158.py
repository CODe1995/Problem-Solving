N,K=map(int,input().split())
lists = list(range(1,N+1))
stk = []
pos=K-1
while lists:
    if len(lists)>pos:
        stk.append(lists.pop(pos))
        pos += K-1  #하나씩 pop 되니까 -1 해줘야함
    else:#pos가 범위보다 커지면
        pos = pos % len(lists)
        stk.append(lists.pop(pos))
        pos += K-1
print('<',end='')
for i,d in enumerate(stk):
    print(d,end='')
    if len(stk)>i+1:
        print(', ',end='')    
print('>')

