import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().rstrip().split()))
answer = [-1]*N
def solve():
    maxnum = 0
    for i in range(len(arr)-1,-1,-1):
        if maxnum<arr[i]:
            answer[i]=-1#제일 큰 수보다 크다면
            maxnum = arr[i]
        else:
            if N>i+1:#범위체크
                if arr[i]<arr[i+1]:#다음 값보다 내가 작다면
                    answer[i] = arr[i+1]
                else:#다음 값보다 내가 크다면
                    for j in range(i+1,N):
                        if arr[j]>arr[i]:
                            answer[i]=arr[j]
                            break
                        if answer[j]>arr[i]:
                            answer[i]=answer[j]
                            break

if __name__=="__main__":
    solve()
    for i in answer:
        sys.stdout.write(str(i)+' ')
