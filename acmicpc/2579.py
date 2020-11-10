n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
cnt = 0

#총 계단 수, 현재 밟고 있는 계단, 현재 점수
def calc(maxS,now,points):
    if maxS-1 == now:  #도착했다면
        return arr[max-1]
    if maxS-1 - now >= 1:
        points = points + max(calc(maxS,i+1,points),calc(maxS,i+2,points))  #한 칸과 두 칸 올라가는 점수 비교
        

    

calc(n,0,0)