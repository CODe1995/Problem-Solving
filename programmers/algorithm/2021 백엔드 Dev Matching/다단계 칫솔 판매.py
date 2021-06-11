graph = {}
result = {}
def init(enroll):
    graph['center']=''
    result['center'] = 0
    for name in enroll:
        graph[name] = ''
        result[name] = 0
def dfs(name,cost):    
    remain = int(cost*0.1)
    if cost*0.1<1:#1원 미만인 경우 혼자 다가짐
        result[name]+=cost
        return    
    mine = cost-remain
    result[name]+=mine
    if graph[name]:#부모가 있다면?
        dfs(graph[name],remain)

def solution(enroll, referral, seller, amount):
    answer = []
    init(enroll)    #그래프 생성 및 초기화

    for i in range(len(referral)):  #그래프 데이터 등록
        parent = referral[i]
        if referral[i]=='-':
            parent = 'center'
        graph[enroll[i]]=parent#부모를 넣어줌(뿌리부터 부모까지 역순으로 올라가게)
    
    for i in range(len(seller)):
        name = seller[i]    #판매자
        earn = amount[i]*100    #수익금
        dfs(name,earn)#정산
    
    for name in enroll:
        answer.append(result[name])
    return answer