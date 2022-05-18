maxDiffScore = 0
answer = [-1]

def solution(n, info):
    global answer
    dfs(0, n, info, [0]*11)
    print(answer)
    return answer

def isALotOfShootSmallerScore(ryanTargetBoard):
    for i in range(10, -1, -1):
        if answer[i] < ryanTargetBoard[i]:
            return True
        elif answer[i] > ryanTargetBoard[i]:
            return False
    

def calcScore(apeachTargetBoard, ryanTargetBoard):
    global maxDiffScore, answer
    apeachScore = 0
    ryanScore = 0
    for i in range(11):
        apeachHits = apeachTargetBoard[i]
        ryanHits = ryanTargetBoard[i]
        if apeachTargetBoard[i] > 0 or ryanTargetBoard[i] > 0:
            if apeachHits >= ryanHits:
                apeachScore += 10-i
            else:
                ryanScore += 10-i
    if ryanScore > apeachScore:
        diffScore = ryanScore - apeachScore
        if maxDiffScore < diffScore:
            maxDiffScore = diffScore
            answer = [s for s in ryanTargetBoard]
        elif maxDiffScore == diffScore and isALotOfShootSmallerScore(ryanTargetBoard):
            answer = [s for s in ryanTargetBoard]



def dfs(depth, remainArrows, apeachTargetBoard, ryanTargetBoard):
    if depth == 11 or remainArrows == 0:
        ryanTargetBoard[10] += remainArrows
        calcScore(apeachTargetBoard, ryanTargetBoard)
        ryanTargetBoard[10] -= remainArrows
        return
    if apeachTargetBoard[depth] < remainArrows:
        ryanTargetBoard[depth] += apeachTargetBoard[depth] + 1
        dfs(depth+1, remainArrows-(apeachTargetBoard[depth]+1), apeachTargetBoard, ryanTargetBoard)
        ryanTargetBoard[depth] -= apeachTargetBoard[depth] + 1
    dfs(depth+1, remainArrows, apeachTargetBoard, ryanTargetBoard)

# assert solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]) == [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0], '오답'
# assert solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [-1]
# assert solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]) == [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0]
# assert solution(9, [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0]) == [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
# assert solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]) == [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2]
solution(3, [0,0,1,0,0,0,0,0,0,1,0])
