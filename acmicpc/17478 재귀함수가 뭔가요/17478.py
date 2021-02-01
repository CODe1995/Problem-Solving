N = int(input())
text = [""]*7
text[0] = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."
text[1] = "\"재귀함수는 자기 자신을 호출하는 함수라네\""
text[2] = "\"재귀함수가 뭔가요?\""
text[3] = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."
text[4] = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
text[5] = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
text[6] = "라고 답변하였지."

def listen(depth):
    udb = '____'*depth
    if(depth==N+1):
        udb = '____'*(depth-1)
        print(udb+text[1])
        return
    print(udb+text[2])
    if(depth!=N):
        print(udb+text[3])
        print(udb+text[4]) 
        print(udb+text[5])   
    listen(depth+1)
    print(udb+text[6])

if __name__=="__main__":
    print(text[0])
    listen(0)