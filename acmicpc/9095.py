from collections import Counter
def calc(nlist):
    lst = []
    for i in nlist:
        if i-1>=0:lst.append(i-1)
        if i-2>=0:lst.append(i-2)
        if i-3>=0:lst.append(i-3)
    lst=list(lst)
    return lst

T=int(input())
for i in range(T):
    n=int(input())
    cnt=0
    rs=[n]
    # print(rs)
    while True:
        tmp=rs
        rs = calc(tmp)
        # print(rs)
        cnt+=Counter(rs)[0] #0의 갯수가 곧 갯수다
        if sum(rs)==0:
            break
    print(cnt)
    