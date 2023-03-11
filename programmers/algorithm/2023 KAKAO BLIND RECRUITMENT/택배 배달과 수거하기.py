# 참고 코드
# https://school.programmers.co.kr/questions/43364


def solution(cap, n, deliveries, pickups):
    answer = 0
    d = 0
    p = 0
    for i in range(n-1, -1, -1):
      cnt = 0
      d -= deliveries[i]
      p -= pickups[i]
      
      while 0 > d or 0 > p:
        d += cap
        p += cap
        cnt += 1
      
      answer += (i+1) * 2 * cnt 
    return answer

a1 = solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0])
print(a1, a1 == 16)

a2 = solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0])
print(a2, a2 == 30)
