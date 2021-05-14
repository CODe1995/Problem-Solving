# # print('123456'.find('7'))
def solution(s):
    answer = []
    
    for cur in s:
        stack = list()
        cnt = 0 #뽑아낸 110의 갯수        
        for i in range(len(cur)):
            stack.append(cur[i])
            if len(stack)>=3:
                temp = stack[-3:]                
                if temp == ['1','1','0']:
                    cnt+=1
                    stack.pop()
                    stack.pop()
                    stack.pop()
        
        for i in range(len(stack)):
            if len(stack)>=3 and stack[i:i+3]==['1','1','1']:#최초 111
                for j in range(cnt):    #110을 뽑은 갯수만큼 삽입
                    stack.insert(i,'0')
                    stack.insert(i,'1')
                    stack.insert(i,'1')
                break
        else:   #111이 존재하지 않는다면?
            for j in range(cnt):    #110을 뽑은 갯수만큼 삽입
                stack.insert(i,'0')
                stack.insert(i,'1')
                stack.insert(i,'1')
                # stack.append('1')
                # stack.append('1')
                # stack.append('0')        
        # print(stack,cnt)
        answer.append(''.join(stack))
    return answer

print(solution(['1110110110110','1110','100111100','0111111010','1111','11100']))
# print(solution(['0111111010']))
# print(solution(['10111111100']))
#1101 100110110 0110110111