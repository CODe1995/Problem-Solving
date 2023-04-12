N = int(input())
arr = list(map(int, input().split()))
s,e = 0,N-1
_sum = abs(arr[s] + arr[e])
answer = [arr[s], arr[e]]

while s < e:
    tmp = arr[s] + arr[e]

    if _sum > abs(tmp):
        _sum = abs(tmp)
        answer = [arr[s], arr[e]]
    if tmp == 0:  # 이미 정답인 결과가 나옴
        break

    if tmp > 0:
        e-=1
    elif tmp < 0:
        s+=1

print(answer[0], answer[1])