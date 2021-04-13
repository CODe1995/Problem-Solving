#북,남,서,동 1,2,3,4

width,height = map(int,input().split())
N = int(input())
arr = list()
for i in range(N+1):
    a,b = map(int,input().split())
    if a==1:arr.append([b,0,a])
    elif a==2:arr.append([b,height,a])
    elif a==3:arr.append([0,b,a])
    else:arr.append([width,b,a])
root = arr.pop()
answer = 0

def isFTF(s1,s2):#서로 마주보는지 
    a,b = min(s1,s2), max(s1,s2)
    if a==1 and b==2:return True
    elif a==3 and b==4:return True
    return False

for i in range(N):
    tx,ty,td = arr[i]
    if isFTF(td,root[2]):
        answer+=(abs(root[0]-tx)+abs(root[1]-ty))*2
    else:
        answer+=abs(root[0]-tx)+abs(root[1]-ty)
print(answer)
    