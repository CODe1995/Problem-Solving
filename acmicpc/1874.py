n = int(input())
pos = 0; high = 0
stk=[]
tmp = [i for i in range(1,n+1)]
# print(tmp)
for i in range(n):
    num = int(input())
    if num>high:
        for _ in range(num-high):stk.append('+')
        pos+=num-high
        high+=num-high
    if tmp[pos-1]==num:#pop        
        pos-=1
        tmp.remove(num)
        stk.append('-')
        # print(tmp)
if tmp:
    print('NO')
else:
    for i in range(len(stk)):
        print(stk[i] )
    
