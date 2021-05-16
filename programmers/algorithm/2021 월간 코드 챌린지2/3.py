# solution https://blog.hoony.me/3

def f(n):
    stk = []
    cnt = 0
    for i in n:
        stk.append(i)
        if i == '0' and stk[-3:] == ['1', '1', '0']:
            del stk[-3:]
            cnt += 1
    idx = -1
    for i in range(len(stk)):
        if stk[i] == '0':
            idx = i
    if idx < 0:
        ret = "110"*cnt + ''.join(stk)
    else:
        ret = ''.join(stk[:idx+1]) + "110"*cnt + ''.join(stk[idx+1:])
    return ret
def solution(s):
    return [f(x) for x in s]

print(solution(['1110110110110','1110','100111100','0111111010','1111','11100']))
# print(solution(['0111111010']))
# print(solution(['10111111100']))
#1101 100110110 0110110111