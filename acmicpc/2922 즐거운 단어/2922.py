word = list(input())
def solution(depth, moum, jaum, l):
    if moum==3 or jaum==3:return 0
    if depth==len(word):
        if l==0:return 0
        else: return 1#유효하면 1을 곱해줌
    total = 0
    if word[depth]!='_':#이미 알파벳 존재
        if word[depth] in 'AEIOU':
            total = solution(depth+1,moum+1,0,l)
        elif word[depth] == 'L':#L
            total = solution(depth+1,0,jaum+1,l+1)
        else:#자음
            total = solution(depth+1,0,jaum+1,l)
    else:    
        total += 5 * solution(depth+1,moum+1,0,l)    #모음
        total += 20 * solution(depth+1,0,jaum+1,l)   #자음
        total += solution(depth+1,0,jaum+1,l+1)  #L
    return total
print(solution(0,0,0,0))