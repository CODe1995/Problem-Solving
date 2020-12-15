def lcs(a,b):
    prev = [0]*len(a)
    for i,r in enumerate(a):
        current = []
        for j,c in enumerate(b):
            if c==r:#좌측 대각선 한칸 + 1
                tmp = prev[j-1]+1 if i*j>0 else 1   #첫 비교부터는 무조건 1이기 때문에 1을 리턴해야함
            else:#같은열 왼쪽껄 따라감
                tmp = max(prev[j] if i>0 else 0,current[-1] if j>0 else 0) #조건 없으면 out of range 뜸
            current.append(tmp)
        prev = current
    return prev[-1]

a = input()
b = input()
print(lcs(a,b))
