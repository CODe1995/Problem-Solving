_DAYS = 28

def convertToDays(date):
    year, month, day = map(int, date.split('.'))
    return year * 12 * 28 + month * 28 + day

def isExpired(todayDays, pastDays, limitDays):
    if (todayDays - pastDays) >= limitDays:
      return True
    return False

def solution(today, terms, privacies):
    answer = []

    todayDays = convertToDays(today)
    termMap = {}

    for term in terms:
      _type, month = term.split()
      termMap[_type] = int(month) * _DAYS

    for index, privacy in enumerate(privacies):
      date, _type = privacy.split()
      targetDays = convertToDays(date)
      if isExpired(todayDays, targetDays, termMap[_type]):
        answer.append(index+1)

    return answer

a1 = solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])
print(a1)

a2 = solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])
print(a2)