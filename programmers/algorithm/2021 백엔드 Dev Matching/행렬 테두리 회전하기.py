field = []

def turn(x1,y1,x2,y2):
    global field
    w = abs(x1-x2)+1
    h = abs(y1-y2)+1
    prev = field[y1+1][x1]
    minnum = prev
    for i in range(w):#상단 회전        
        cur = field[y1][x1+i]
        field[y1][x1+i] = prev
        prev = cur
        minnum = min(minnum,prev)
    for i in range(1,h):#우측 회전
        cur = field[y1+i][x2]
        field[y1+i][x2] = prev
        prev = cur     
        minnum = min(minnum,prev)   
    for i in range(1,w):#하단 회전
        cur = field[y2][x2-i]
        field[y2][x2-i] = prev
        prev = cur
        minnum = min(minnum,prev)
    for i in range(1,h):#좌측 회전
        cur = field[y2-i][x1]
        field[y2-i][x1] = prev
        prev = cur   
        minnum = min(minnum,prev)
    return minnum
def solution(rows, columns, queries):
    global field
    answer = []
    num = 1   
    for i in range(rows):
        col = []
        for j in range(columns):
            col.append(num)
            num+=1
        field.append(col)
     
    for query in queries:
        y1,x1,y2,x2 = query
        x1-=1
        y1-=1
        x2-=1
        y2-=1   #좌표 일치시켜줌
        answer.append(turn(x1,y1,x2,y2))
        # test(query)
    return answer