def solve(s):
    ret = ''
    for i in range(len(s)):
        if i==0 or (s[i-1]==' ' and s[i]!=' '):
            ret+=s[i].upper()
        else:
            ret+=s[i]
    return ret

print(solve('hello   world  lol'))