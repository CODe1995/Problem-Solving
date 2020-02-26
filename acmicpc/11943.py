buc1,buc2=(list(map(int,input().split()))for _ in range(2))
print(min(buc1[0]+buc2[1],buc1[1]+buc2[0]))