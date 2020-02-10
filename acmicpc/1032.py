N=int(input())
st=input().split()
global result
result = st[0]
for i in range(N-1):
    if N > 1:
        for j in range(len(st[0])):            
            # print('i값 : ',i,'j값 : ',j,'st[i+1][j] : ',st[i+1][j],'result[j] : ',result[j])
            if result[j]==st[i+1][j]:
                result = result[:j]+st[i][j]
            else:
                result = result[:j]+'?'
            # print(st[i][j],"비교",st[i+1][j],'결과',result)
print(result)