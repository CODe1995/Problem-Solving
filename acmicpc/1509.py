def palindrome(t):
    if len(t)==1: print(t)
    elif len(t)==2 and t[0]==t[1]: print(t)
    else:
        if(t[0]==t[-1]):
            print(t)
            return palindrome(t[1:-1])
        else:
            return False
# t = input()
t= 'ABACABA'
dp = [[0]*len(t) for _ in range(len(t)+1)]
print(palindrome(t))



