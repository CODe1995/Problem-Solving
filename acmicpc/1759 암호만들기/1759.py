from itertools import combinations
L,C = map(int,input().split())#l 자릿수 c개문자 주어짐
arr = input().split()
arr.sort()
cmbs = combinations(arr,L)
for cmb in cmbs:
    vo=0
    for c in cmb:
        if c in 'aeiou':
            vo+=1
    if 1<=vo<=L-2:
        print(''.join(cmb))