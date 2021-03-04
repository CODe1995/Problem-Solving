import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
dodq = deque()  #도도덱
sudq = deque()  #수연덱
do_grdq = deque()   #도도 그라운드
su_grdq = deque()   #수연 그라운드
for _ in range(N):
    a,b = map(int,input().split())
    dodq.appendleft(a)
    sudq.appendleft(b)
gameTime = 0
winFlag = -1#0 도도승, 1 수연승, 2 비김
def initGround():#그라운드 초기화
    su_grdq=deque()
    do_grdq=deque()
while M!=gameTime:#M번 진행
    if gameTime%2==0:#도도 턴
        do_grdq.appendleft(dodq.popleft())#left에 넣어주면 reverse를 할 필요가 없어짐
    else:#수연 턴
        su_grdq.appendleft(sudq.popleft())

    #덱 비었는지 체크
    if not dodq or not sudq:
        break

    #그라운드 안비어있고 합 5
    win = -1
    if su_grdq and do_grdq and su_grdq[0]+do_grdq[0]==5:#수연종
        win = 1
    if (su_grdq and su_grdq[0]==5) or (do_grdq and do_grdq[0]==5):#도도종   
        win = 2
    if win!=-1:#승부가 난 경우 덱의 이동
        if win==1:
            while do_grdq:sudq.append(do_grdq.pop())
            while su_grdq:sudq.append(su_grdq.pop())
        elif win==2:
            while su_grdq:dodq.append(su_grdq.pop())
            while do_grdq:dodq.append(do_grdq.pop())
    gameTime+=1

# print(dodq,sudq)
if len(dodq)>len(sudq):winFlag=0
elif len(dodq)<len(sudq):winFlag=1
else:winFlag=2
print(['do','su','dosu'][winFlag])