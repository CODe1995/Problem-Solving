import sys
input = sys.stdin.readline
  


N = int(input().rstrip())
# stairs_state = [[0] for _ in range(N-1)]
stairs = dict()
scores_state = []
for i in range(N):
    scores_state.append(int(input().rstrip()))
cnt = 0

root = []
#경로를 구함

solution([0],0,True)
#현재까지 밟아온 계단, 몇번째 배열인지 idx, 연속건너기 가능한지 가능하면T 불가능F
def solution(current,idx,successive=True):
    if current[-1] == N: return current
    if successive == True and N-2>=current[-1]:  #연속밟기
        current.append(current[-1]+1)   #마지막계단 +1
        successive=False    #연속밟기 불가능하게 바꿈
        solution(current,idx,jump)
    else if

    

