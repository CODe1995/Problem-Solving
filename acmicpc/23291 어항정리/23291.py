N, K = map(int, input().split())
fishbowl = list(map(int, input().split()))

# 가장 적은 곳에 물고기 넣기
def pushFish():
    global fishbowl
    minFishCnt = min(fishbowl)
    for i in range(len(fishbowl)):
        if fishbowl[i] == minFishCnt:
            fishbowl[i] += 1

