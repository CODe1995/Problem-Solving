# 총 합이 100이어야함.
T = []
for i in range(9):
    T.append(int(input()))
T=sorted(T)
flag=False
for i in range(9):
    for j in range(i,9):
        if (sum(T)-T[i]-T[j] == 100):   
            temp = T[j] 
            T.remove(T[i])  
            T.remove(temp)           
            flag=True
            break
    if(flag==True):
        break
for i in T:
    print(i)