answer = 0
def solution(numbers, target):
    global answer, sumArr
    dfs(0,numbers,0,target)
    return answer

def dfs(depth,numbers,sumnum,target):
    global answer
    if depth==len(numbers):
        if sumnum==target:
            answer+=1
        return    
    dfs(depth+1,numbers,sumnum+numbers[depth],target)
    dfs(depth+1,numbers,sumnum-numbers[depth],target)