while True:
    datas=list(map(str,input()))
    if len(datas)==1 and datas[0]=='.':break
    stk=[]
    for j in datas:
        if j in ('(',')','[',']'):
            stk.append(j)
            tmp = stk[len(stk)-2]+j
            if tmp in ('()','[]'):
                stk.pop()
                stk.pop()
    if len(stk)==0:
        print('yes')
    else:print('no')       
    