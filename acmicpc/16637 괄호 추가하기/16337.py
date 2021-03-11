import sys
from collections import deque
N = int(input())
arr = list(input().strip())
stackNum = deque()
stackOper = deque()
for i in range(N):
    if 0<=ord(arr[i])-48<=9:#숫자라면
        stackNum.append(int(arr[i]))
    else:
        stackOper.append(arr[i])
#ASCII 0~9 : 48~57 : -48
res = stackNum.popleft()#첫번째 숫자는 결과에 넣어둠
operSize = len(stackOper)
numSize = len(stackNum)
while stackNum or stackOper:#둘 중 하나라도 남아있으면 계속 반복        
    if stackOper[0]=='+':
        #덧셈이라면 무조건 선계산
        stackOper.popleft()
        operSize-=1
        res += stackNum.popleft()
        numSize-=1
    elif stackOper[0]=='*':
        if operSize>1 and stackOper[1]=='+' and numSize>=2:#뒤가 덧셈이면 얘먼저:#뒤가 더있다?                
            tmp = stackNum[0]+stackNum[1]
            res*=tmp
            stackNum.popleft()
            stackNum.popleft()
            numSize-=2
            stackOper.popleft()
            stackOper.popleft()
            operSize-=2
        else:
            res*=stackNum.popleft()
            stackOper.popleft()
            numSize-=1
            operSize-=1
    elif stackOper[0]=='-':
        if operSize>=3 and stackOper[1]=='-' and stackOper[2]=='-' and numSize>=3:
            front_tmp = res-stackNum[0]-stackNum[1]-stackNum[2]#순차계산
            middle_tmp = res-(stackNum[0]-stackNum[1])-stackNum[2]
            back_tmp = res-stackNum[0]-(stackNum[1]-stackNum[2])                    
            if middle_tmp<back_tmp:#뒤가 더 이득이면 그대로 계산
                res -= stackNum[0]
                stackNum.popleft()
                stackOper.popleft()
                numSize-=1
                operSize-=1
            else:
                res -= (stackNum[0]-stackNum[1])
                stackOper.popleft()
                stackNum.popleft()
                stackOper.popleft()
                stackNum.popleft()
                numSize-=2
                operSize-=2
        else:
            if operSize>=2 and stackOper[1]=='-' and numSize>=2:
                front_tmp = res-stackNum[0]-stackNum[1]#순차계산
                back_tmp = res-(stackNum[0]-stackNum[1])
                if front_tmp<back_tmp:#뒤가 더 이득
                    res -= (stackNum[0]-stackNum[1])
                    stackNum.popleft()
                    stackOper.popleft()
                    stackNum.popleft()
                    stackOper.popleft()
                    numSize-=2
                    operSize-=2
                else:
                    res-=stackNum.popleft()
                    stackOper.popleft()
                    numSize-=1
                    operSize-=1        
            else:
                res-=stackNum.popleft()
                stackOper.popleft()
                numSize-=1
                operSize-=1
print(res)