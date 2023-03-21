# 2023.03.21
from enum import Enum

class Hand(Enum):
    RIGHT = 'right'
    LEFT = 'left'

RIGHT_PAD = [3,6,9]
LEFT_PAD = [1,4,7]

def getX_Y(number):
    return [(number-1)%3, (number-1)//3]

def getCloserHand(left, right, nextNumber, hand):
    lx, ly = getX_Y(left)
    nx, ny = getX_Y(nextNumber)
    rx, ry = getX_Y(right)

    leftDistance = abs(ly-ny) + abs(lx-nx)
    rightDistance = abs(ry-ny) + abs(rx-nx)
    
    if leftDistance < rightDistance:
        return Hand.LEFT
    elif leftDistance > rightDistance:
        return Hand.RIGHT
    else:
        if hand == Hand.LEFT._value_:
            return Hand.LEFT
        return Hand.RIGHT
    

def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for number in numbers:
        if number == 0:
            number = 11
        if number in RIGHT_PAD:
            right = number
            answer += 'R'
        elif number in LEFT_PAD:
            left = number
            answer += 'L'
        else:
            nextHand = getCloserHand(left, right, number, hand)
            if nextHand == Hand.LEFT:
                left = number
                answer += 'L'
            else:
                right = number
                answer += 'R'
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))