# 전위 중위 후위로 출력
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    
class Tree:
    def __init__(self):
        self.root = None
    #자식노드가 비어있다면 넘어감
    def preT(self, node):#DLR 전위
        print(node,end='')
        if not node.left == None:self.preT(node.left)
        if not node.right == None : self.preT(node.right)
    def inT(self,node):#LDR 중위
        if not node.left == None:self.inT(node.left)
        print(node,end='')
        if not node.right== None:self.inT(node.right)
    def postT(self,node):#LRD 후위
        if not node.left == None : self.postT(node.left)
        if not node.right == None : self.postT(node.right)
        print(node,end='')
    
    def initRoot(self,node,left_node,right_node):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node

if __name__ == "__main__":
    node = []
    N = int(input())
    for i in range(N):
        #root left right 순으로 입력 없으면 .
        
        


    m_tree = Tree()
    for i in range(int(len(node)/2)):
        m_tree.initRoot(node[i],node[i*2+1],node[i*2+2])
    m_tree.preT(m_tree.root)
    m_tree.inT(m_tree.root)
    m_tree.postT(m_tree.root)