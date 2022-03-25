class Node():
    def __init__(self):
        self.data=None
        self.link=None

def printNodes(start):
    current=start
    if current==None:
        return
    print(current.data,end=' ')
    while current.link != None:
        current =current.link
        print(current.data, end=' ')

    
def makeSimpleLinkedList(name):
    global memory, head,current,pre

    node=Node()
    node.data=name
    memory.append(node)
    if head==None:
        head=node
        return
    
    
    current=head
    while current.link!=None:
        pre= current
        current=current.link
        
    
    current.link=node

def findNode(findData):
    global memory,head,current,pre

    current=head
    if current.data==findData:
        return current
    while current.link!=None:
        current=current.link
        if current.data==findData:
            return current
    return 0


def deleteNode(deleteData):
    global memory,head,current,pre

    if head.data==deleteData:
        pre=head
        while pre.link!=None:
            current=pre
            pre=pre.link
            current.data=None
        pre.data=None
        return
    
    current=head
    while current.link!=None:
        pre=current
        current=current.link
        if current.data==deleteData:
            while current.link!=None:
                current.data=None
                pre=current
                current=current.link
            current.data=None
    return



memory=[]
head, current, pre = None, None,None

if __name__=="__main__":

    for i in range(0,6):
        name=input()
        if name=="" or name==None:
            break
        makeSimpleLinkedList(name)
    
        
    fNode=findNode(input())
    if fNode==0:
        print("X")
    else:
        deleteNode(fNode.data)
        printNodes(head)

        