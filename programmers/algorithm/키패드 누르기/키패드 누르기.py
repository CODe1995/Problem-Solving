def solution(numbers, hand):
    answer = ''
    left = 10#현재 왼손 위치
    right = 12#현재 오른손 위치
    for i in range(len(numbers)):
        cur = numbers[i]
        if cur in [1,4,7]:
            answer+='L'
            left = 11 if cur==0 else cur
        elif cur in [3,6,9]:
            answer+='R'
            right = 11 if cur==0 else cur
        else:
            #누가 더 가깝나?
            #각 손의 좌표 파악
            lx = (left-1)%3
            ly = (left-1)//3
            rx = (right-1)%3
            ry = (right-1)//3
            
            #목적지
            tx = ((11 if cur==0 else cur)-1)%3
            ty = ((11 if cur==0 else cur)-1)//3
            
            ld = abs(ty-ly) + abs(tx-lx)
            rd = abs(ty-ry) + abs(tx-rx)
            
            if ld<rd or (ld==rd and hand=='left'):
                answer+='L'
                left = 11 if cur==0 else cur
            elif ld>rd or (ld==rd and hand=='right'):
                answer+='R'
                right = 11 if cur==0 else cur
            # print(lx,ly,rx,ry)
    return answer