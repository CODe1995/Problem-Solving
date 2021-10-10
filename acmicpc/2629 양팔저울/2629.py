N = int(input())
weights = [0] * 31
inp = list(map(int, input().split()))
for i in range(N):
    weights[i] = inp[i]
dp = [[0] * 15002 for _ in range(32)]


def solution(index, weight):
    global weights, dp, N
    if index > N or dp[index][weight]: return
    dp[index][weight] = 1
    solution(index + 1, weight + weights[index])
    solution(index + 1, weight)
    solution(index + 1, abs(weight - weights[index]))


M = int(input())
marbles = list(map(int, input().split()))
answer = []
solution(0, 0)
for i in range(M):
    if marbles[i] > 15000:
        answer.append('N')
    elif dp[N][marbles[i]]:
        answer.append('Y')
    else:
        answer.append('N')
print(' '.join(answer))
