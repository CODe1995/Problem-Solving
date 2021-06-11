def getRank(num):
    res = [6,6,5,4,3,2,1]
    return res[num]
def solution(lottos, win_nums):
    answer = []
    zero = 0
    for i in lottos:
        if i==0:
            zero+=1
    cor = 0
    for i in lottos:
        for j in win_nums:
            if i==j:
                cor+=1
    return [getRank(zero+cor),getRank(cor)]