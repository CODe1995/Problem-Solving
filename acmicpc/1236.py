height,width = map(int,input().split())
castle = []
for _ in range(height):
    s=list(input())
    castle.append(s)
cRow=[]
cCol=[]
for i in range(height):
    cRow.append('X' not in castle[i])
for j in range(width):
    cCol.append('X' not in [castle[i][j] for i in range(height)])
print(max(sum(cRow),sum(cCol)))