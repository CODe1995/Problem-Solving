def convertToN(n, k):
    cn = ''
    while(n>0):
        n, mod = divmod(n, k)
        cn += str(mod)
    return cn[::-1]

def isPrime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(n, k):
    answer = 0
    n = convertToN(n,k) if k!=10 else str(n)
    for s in n.split('0'):
        if s != '' and isPrime(int(s)):
            answer+=1
    return answer