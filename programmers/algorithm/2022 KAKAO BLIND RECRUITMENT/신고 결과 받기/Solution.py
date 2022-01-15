def solution(id_list, report, k):
    reportList = {name: 0 for name in id_list}
    mailList = {name: list() for name in id_list}   # 메일 전송을 위해, 신고자:{피신고자...} 형태로 생성
    report = list(set(report))  # 중복 제거

    for i in range(len(report)):
        reporter, reportee = report[i].split()  # 신고자, 피신고자
        mailList[reporter].append(reportee)
        reportList[reportee] += 1

    # 메일 출력을 위한 구문
    answer = [0]*len(id_list)
    for i in range(len(id_list)):
        name = id_list[i]
        for reportee in mailList[name]:  # 내가 신고한 사람의 명단
            if reportList[reportee] >= k:  # 신고 횟수 초과한 사람이라면
                answer[i] += 1
    return answer
