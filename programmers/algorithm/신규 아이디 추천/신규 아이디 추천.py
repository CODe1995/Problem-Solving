import re
def solution(new_id):    
    #1단계 & 2단계 소문자 치환, 제거
    answer = re.sub('[^0-9a-z_.\-]+','',new_id.lower())
    
    #3단계 . 2번 이상을 1개로 압축
    answer = re.sub('\.\.+','.',answer)
    
    #4단계 양끝 . 제거
    answer = answer.strip('.')
    
    #5단계 빈문자열 a 추가
    if answer =='': answer='a'
        
    #6단계 15개제외하고 문자모두제거, 우측 . 제거
    answer = answer[:15].rstrip('.')
        
    #7단계 길이 3 될 때까지 끝 문자 추가    
    answer+=answer[-1]*(3-len(answer))
        
    return answer