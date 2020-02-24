import sys
T = int(input())
for i in range(T):
    datas = list(map(str,sys.stdin.readline().rstrip()))
    #괄호가 닫히는 순간 POP
    stk=[]
    for j in datas:
        stk.append(j)
        if j==')' and stk[len(stk)-2]=='(':
            stk.pop()
            stk.pop()
    if len(stk):
        print('NO')
    else:
        print('YES')

