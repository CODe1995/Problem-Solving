#2진법 풀이 추가#
# 5 -> bin) 101 즉, 1의 개수를 의미한다.
# 23 -> bin) 10111 갯수는 4개가 된다.
# 따라서 2로 나누었을때 1의 갯수만 파악하면 됌
X=int(input())
cnt = 0
while X != 0:
    if X%2==1:
        cnt+=1
    X=X//2
print(cnt)
## 2020.02.23
# sticks = [64]
# while sum(sticks)!=X:
#     if sum(sticks)>=X:
#         temp = sticks[len(sticks)-1]
#         sticks.remove(temp)        
#         sticks.append(temp//2)
#         sticks.append(temp//2)
#         if sum(sticks)-temp//2>=X:
#             sticks.remove(temp//2)
# print(len(sticks))