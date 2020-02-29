import collections
n = int(input())
card=collections.deque(list(i for i in range(1,n+1)))

while len(card)>1:
    card.popleft()#맨 앞 하나빼고
    card.rotate(-1)#맨 앞 뒤로넣고
print(card[0])
    