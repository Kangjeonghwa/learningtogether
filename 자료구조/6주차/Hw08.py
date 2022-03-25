# 교과서 199   응용예제 2

class Node():
    def __init__(self):
        self.plink=None
        self.data=None
        self.nlink=None

def printNodes(start):
    current=start
    if current.nlink==None:
        return
    print("정방향-->",end=' ')
    print(current.data, end=' ')
    while current.nlink!=None:
        current=current.nlink
        print(current.data, end=' ')
    print()

def printNodes2(start):
    current=start
    if current.plink==None:
        return

    print("역방향-->", end=' ')
    print(current.data, end=' ')
    while current.plink!=None:
        current=current.plink
        print(current.data, end=' ')
    print()

memory=[]
head, current, pre, last =None,None,None,None
dataArray=["다현","정연","쯔위","사나","지효"]

if __name__=="__main__":

    node=Node()
    node.data=dataArray[0]
    head=node
    memory.append(node)

    for data in dataArray[1:]:
        pre=node
        node=Node()
        node.data=data
        pre.nlink=node
        node.plink=pre
        memory.append(node)
        last=node
    
    printNodes(head)
    printNodes2(last)
        

