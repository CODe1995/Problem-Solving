def solution(id_list, report, k):
    reportList = {}
    mailList = {}   # 메일 전송을 위해, 신고자:{피신고자...} 형태로 생성
    visited = {}    # 1인 중복 신고 방지
    
    for id in id_list:  # 초기화
        reportList[id] = 0
        mailList[id] = list()                
    
    for i in range(len(report)):
        if(report[i] in visited):
            continue
        reporter,reportee = report[i].split()  #신고자, 피신고자
        visited[report[i]] = 1            
        mailList[reporter].append(reportee)
        reportList[reportee] += 1
        
    # 메일 출력을 위한 구문
    answer = [0]*len(id_list)
    for i in range(len(id_list)):
        name = id_list[i]
        for reportee in mailList[name]: # 내가 신고한 사람의 명단
            if reportList[reportee] >= k:    #신고 횟수 초과한 사람이라면
                answer[i] += 1
    return answer