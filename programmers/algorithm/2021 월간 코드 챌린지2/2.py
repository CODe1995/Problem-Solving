def f(n):
    strn = list(str(bin(n)))
    flag = False
    for i in range(len(strn[2:])-1,-1,-1):
        if strn[i+2]=='0':            
            strn[i+2]='1'
            if len(strn)>i+3:
                strn[i+3]='0'
            flag=True
            break
    if not flag:
        strn[2]='0'
        strn.insert(2,'1')
    strn = ''.join(strn)
    return int(strn,2)

def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(f(num))
    return answer

print(solution([4,5]))