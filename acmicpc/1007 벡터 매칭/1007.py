import sys
input = sys.stdin.readline
visited = list()
arr = list()
N = 0
answer = 10e9
def calc():
    pos = [0,0]#벡터
    for i in range(N):
        if visited[i]:
            pos[0] += arr[i][0]
            pos[1] += arr[i][1]
        else:
            pos[0] -= arr[i][0]
            pos[1] -= arr[i][1]
    vector = (pos[0]**2+pos[1]**2)**0.5
    return vector

def combination(depth,index):
    global answer
    if N/2==depth:#끝도달
        answer = min(answer,calc())
        return
    for i in range(index,N):
        visited[i]=True
        combination(depth+1,i+1)
        visited[i]=False

if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        answer = 10e9
        N = int(input())
        visited = [False]*N
        arr = [list(map(int,input().strip().split())) for _ in range(N)]
        combination(0,0)
        print("%.12f"%answer)