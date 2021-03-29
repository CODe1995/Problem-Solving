T = int(input())
arr = [list(input()) for _ in range(T)]


def calc(string,s,e,choice):#왼쪽회문
    chance = False
    while(s<=e):
        if string[s]==string[e]:
            s+=1; e-=1
            continue
        if not chance:#유사회문 시도
            if choice=="L" and string[s+1]==string[e]:#왼쪽유사회문
                chance = True
                s+=2; e-=1
                continue
            elif choice=="R" and string[s]==string[e-1]:
                chance = True
                s+=1; e-=2
                continue
        return 2#둘다 아닌 경우    
    if chance:
        return 1#유사회문
    else:
        return 0#회문
for target in arr:
    s,e = 0,len(target)-1
    left = calc(target,s,e,"L")
    right = calc(target,s,e,"R")
    if(left==0 or right==0):print(0)
    elif(left==1 or right==1):print(1)#둘중 하나라도 1이면
    else:print(2)
