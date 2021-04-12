T = int(input())
direction = [[0,0],[0,-1],[1,0],[0,1],[-1,0]]
for t in range(1,T+1):
    posA=[1,1]; posB=[10,10]
    M,A = map(int,input().split())
    ma = list(map(int,input().split()))
    mb = list(map(int,input().split()))
    aps = [list(map(int,input().split())) for _ in range(A)]
    aps = sorted(aps,key = lambda x:-x[3])
    answer = 0
    for time in range(M+1):
        al = list(); bl=list()
        for idx in range(len(aps)):
            if abs(aps[idx][0]-posA[0])+abs(aps[idx][1]-posA[1])<=aps[idx][2]:al.append(idx)
            if abs(aps[idx][0]-posB[0])+abs(aps[idx][1]-posB[1])<=aps[idx][2]:bl.append(idx)
        curmax = 0
        if al or bl:
            if al and bl:
                if al[0]==bl[0]:
                    if len(al)>1:curmax = max(curmax, aps[al[1]][3]+aps[bl[0]][3])
                    if len(bl)>1:curmax = max(curmax, aps[bl[1]][3]+aps[al[0]][3])
                else:
                    curmax = max(curmax, aps[al[0]][3]+aps[bl[0]][3])
            if al:curmax = max(curmax,aps[al[0]][3])
            if bl:curmax = max(curmax,aps[bl[0]][3])
        answer += curmax
        if time==M:continue
        posA[0]+=direction[ma[time]][0]
        posA[1]+=direction[ma[time]][1]
        posB[0]+=direction[mb[time]][0]
        posB[1]+=direction[mb[time]][1]
    print('#{} {}'.format(t,answer)) 