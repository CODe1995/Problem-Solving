# # print('123456'.find('7'))
def solution(s):
    answer = []
    
    for cur in s:
        visited = dict()
        nextIdx = 0
        nextTIdx = 0
        lcur = list(cur)
        while True:
            if cur in visited:
                answer.append(cur)
            visited[cur]=True            
            tidx = cur.find('111',nextTIdx)  #옮겨야 하는 위치            
            if tidx > -1:# 111이 있을때
                idx = cur.find('110',nextIdx)   #110 위치
                nextIdx = tidx+3
                
                if idx<tidx:#111이 뒤에 있는 경우? = 바꾸면 손해임
                    break
                if idx==-1 or nextIdx>=len(cur):# 110 없다면?
                    break

                nextTIdx = tidx+3
                #-- 위치 swap
                lcur[idx]='1'
                lcur[idx+1]='1'
                lcur[idx+2]='1'
                lcur[tidx]='1'
                lcur[tidx+1]='1'
                lcur[tidx+2]='0'
                #--
                cur = ''.join(lcur)
                

            else:   #옮길 필요가 없음
                break    
        answer.append(cur)
    return answer

print(solution(['1110110110110','1110','100111100','0111111010','1111','11100']))
# print(solution(['0111111010']))
#1101 100110110 0110110111