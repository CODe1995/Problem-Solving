def solution(sizes):
    maxW = 0
    maxH = 0
    for w, h in sizes:
        maxW = max(maxW, max(w,h))
        maxH = max(maxH, min(w,h))
    answer = maxW * maxH
    return answer