import sys
data =[]
for i in range(5):
    data.append(int(sys.stdin.readline().rstrip()))
print(sum(data))