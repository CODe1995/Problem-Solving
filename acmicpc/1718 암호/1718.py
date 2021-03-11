a = input()#평
b = input()#암
while len(a)>len(b):
    b*=2
for i in range(len(a)):
    if a[i]!=' ':
        c = ord(a[i])-(ord(b[i])-97)-1
        if c<97:
            c=ord('z')+(c-97)+1
        print(chr(c),end='')
    else:
        print(' ',end='')