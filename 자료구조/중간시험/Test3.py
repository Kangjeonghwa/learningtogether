class Node():
    def __init__(self):
        self.plink=None
        self.data=None
        self.nlink=None

def makeSimpleLinkedList(name):
    global memory, head,current,pre,last

    node=Node()
    node.data=name
    memory.append(node)
    if head==None:
        head=node
        return
    
    
    current=head
    while current.nlink!=None:
        pre= current
        current=current.nlink
        
    
    current.nlink=node
    node.plink=current


def printNodes(start):
    current=start
    if current.nlink==None:
        return
    print(current.data, end=' ')
    while current.nlink!=None:
        current=current.nlink
        print(current.data, end=' ')
    print()
    print(current.data,end=' ')
    while current.plink!=start:
        current=current.plink
        print(current.data, end=' ')
    current=current.plink
    print(current.data, end=' ')

def findNode(findData):
    global memory,head,current,pre,last

    current=head
    if current.data==findData:
        return current
    while current.nlink!=None:
        current=current.nlink
        if current.data==findData:
            return current
    return 0


memory=[]
head, current, pre, last =None,None,None,None

if __name__=="__main__":

    for i in range(0,5):
        name=input()
        if name=="" or name==None:
            break
        makeSimpleLinkedList(name)
    
    fNode=findNode(input())
    if fNode==0:
        print("X")
    else:
        printNodes(fNode)

