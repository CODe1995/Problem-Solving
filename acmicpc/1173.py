N,m,M,T,R = map(int,input().split())
#운동 N분, 최소맥박 m, 최대맥박M, 운동하면 맥박증가 T, 쉬면 맥박감소 R

cur_m = m   #초기 맥박
n = 0   #현재 운동한 시간
cnt = 0 #흐른 시간
if m+T > M or R==0: #불가능한경우
    print(-1)
else:
    while n<N:
        if cur_m+T <= M and n<N:
            cur_m+=T
            n+=1
            cnt+=1
            # print('운동',n,cnt,cur_m)
        else:
            if cur_m-R <m:
                cur_m=m
            else:
                cur_m-=R
            cnt+=1
            # print('휴식',n,cnt,cur_m)

    print(cnt)