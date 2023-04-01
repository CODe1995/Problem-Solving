# 조건을 보면 결국 i는 i-1, i+1과 달라야 한단 뜻이어서 사실상 첫번째 두번째 조건은 크게 의미 없음
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(1,N):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]
print(min(arr[i]))