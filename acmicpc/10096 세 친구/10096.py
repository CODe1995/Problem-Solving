import sys
input = sys.stdin.readline

def solution():    
    N = int(input())
    U = input().rstrip()
    #홀수가 아닌 경우(2*len(S)+1(T)를 생각하면 무조건 홀수개)
    if N%2==0:return 'NOT POSSIBLE'

    ulen = N//2 #S의 크기        
    # 유일하지 않은 경우
    # 1. ABABA
    # 2. ABCABCA
    if U[:ulen]==U[ulen:-1] and U[1:ulen+1]==U[ulen+1:]:
        return "NOT UNIQUE"
    
    # 왼쪽~가운데에 T가 있는 경우
    # 1. TABAB
    # 2. ATBAB
    # 3. ABTAB
    for i in range(ulen):
        if U[i]!=U[ulen+1+i]:#다른 경우, 한칸 앞을 비교
            # print(U[i+1:ulen+1],U[ulen+1+i:])
            if U[i+1:ulen+1]==U[ulen+1+i:]:#앞에건 같으니까 뒤에 남은거만 비교
                return U[ulen+1:]
            else:break#이건 오른쪽에 위치한단 뜻                
    else:#정확히 중간에 T가 위치함
        return U[:ulen]

    # 오른쪽~끝에 T가 있는 경우
    # 1. ABATB
    # 2. ABABT
    for i in range(ulen):
        if U[i]!=U[ulen+i]:            
            # print(U[i:ulen],U[ulen+i+1:])
            if U[i:ulen]==U[ulen+i+1:]:#오른쪽으로 한칸
                return U[:ulen]
            else:
                return 'NOT POSSIBLE'
    else:#맨 끝에 T가 위치하는 경우
        return U[:ulen]

if __name__ == "__main__":
    print(solution())