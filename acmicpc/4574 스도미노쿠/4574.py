import sys
from copy import deepcopy
# sys.stdin = open("C:/Users/code/source/repos/acmicpc/acmicpc/4574 스도미노쿠/input.txt")
input = sys.stdin.readline

N = 1
field = []
sudominoku = []
pairCnt = 0
exist = []
remain = 0
direction = [[0,1],[1,0],[-1,0],[0,-1]]
answerFlag = False

def analysisPosition(line): # B3 -> [3,1]
    return [int(line[1])-1,ord(line[0])-65]

def init():
    global N, field, exist, sudominoku, pairCnt, remain, answerFlag
    N = int(input())        
    if N ==0:return False
    answerFlag = False
    exist = [0]*100
    remain = 81 - (N*2+9)
    sudominoku = [[-1]*9 for _ in range(9)]
    pairCnt = 0
    field = [[-1]*9 for _ in range(9)]
    for i in range(N):
        num1, pos1, num2, pos2 = input().strip().split()
        pos1 = analysisPosition(pos1)
        pos2 = analysisPosition(pos2)
        field[pos1[1]][pos1[0]] = int(num1)
        field[pos2[1]][pos2[0]] = int(num2)
        exist[int(num1+num2)]=1
        exist[int(num2+num1)]=1
        sudominoku[pos1[1]][pos1[0]] = 1
        sudominoku[pos2[1]][pos2[0]] = 1
        pairCnt+=1
    oneToNine = input().strip().split()
    for i in range(9):
        pos = analysisPosition(oneToNine[i])
        field[pos[1]][pos[0]] = i+1
        sudominoku[pos[1]][pos[0]] = 1
    for i in range(11,100,11):#뒤집어도 같은 수 제거
        exist[i]=1
    return True

def rowCheck(row,num):
    global field
    return not num in field[row]    #들어있으면 False

def colCheck(col,num):
    global field
    for i in range(9):
        if num == field[i][col]:
            return False
    return True

def sectionCheck(x,y,num):
    global field
    px,py = x//3, y//3
    for i in range(py*3,py*3+3):
        for j in range(px*3,px*3+3):
            if field[i][j] == num:
                return False
    return True

def printAnswer():
    for i in range(9):
        print(''.join(str(_) for _ in field[i]))
        


def dfsSudominoku(depth,position):    
    global field, sudominoku, exist, pairCnt, answerFlag
    if answerFlag:return
    x,y = position%9, position//9
    if depth+pairCnt == 35:
        printAnswer()  
        answerFlag = True        
        return
    if sudominoku[y][x]>-1:
        dfsSudominoku(depth,position+1)
        return
    sudominoku[y][x]=depth+pairCnt
    for dx,dy in direction:
        nx,ny = x+dx, y+dy
        if 0<=nx<9 and 0<=ny<9 and sudominoku[ny][nx]==-1:
            strnum1 = int(str(field[ny][nx])+str(field[y][x]))
            strnum2 = int(str(field[y][x])+str(field[ny][nx]))
            if exist[strnum1]==1:
                continue
            exist[strnum1] = 1
            exist[strnum2] = 1
            sudominoku[ny][nx]=depth+pairCnt
            dfsSudominoku(depth+1,position+1)
            if answerFlag:return
            sudominoku[ny][nx]=-1
            exist[strnum1] = -1
            exist[strnum2] = -1    
    sudominoku[y][x]=-1
                
def dfs(depth,position):
    global field, answerFlag, remain
    if answerFlag:return
    if depth == remain:        
        dfsSudominoku(0,0)
        return
    x,y = position%9, position//9
    if field[y][x]>-1:
        dfs(depth,position+1)
        return               
    for num in range(1,10):
        section_check = sectionCheck(x,y,num)
        if not section_check:continue
        row_check = rowCheck(y,num)
        if not row_check:continue
        col_check = colCheck(x,num)
        if not col_check:continue
        field[y][x] = num
        dfs(depth+1,position+1)
        if answerFlag:return
        field[y][x] = -1

def solution():
    global field    
    for i in range(9):
        for j in range(9):
            if field[i][j]==-1:
                dfs(0,0)
                return

gameCount = 1
while init():    
    print('Puzzle',gameCount)   
    solution()    
    gameCount+=1
    
        


