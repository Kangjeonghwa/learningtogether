# 교과서 195   응용예제 1

import random
import math

class Node():
    def __init__(self):
        self.data=None
        self.link=None

def printNodes(start):
    current=start
    if current.link==None:
        return
    print(current.data[0],"편의점, 거리: ",math.sqrt(current.data[1]**2+current.data[2]**2) )
    while current.link!=start:
        current=current.link
        print(current.data[0],"편의점, 거리: ",math.sqrt(current.data[1]**2+current.data[2]**2) )
    print()

def makeStoreList(store):
    global head,current,pre,memory

    node=Node()
    node.data=store
    memory.append(node)

    if head==None:
        head=node
        node.link=head
        return
    
    nodeX, nodeY=node.data[1:]
    nodeDist=math.sqrt(nodeX*nodeX+nodeY*nodeY)
    headX,headY=head.data[1:]
    headDist=math.sqrt(headX**2+headY**2)

    if nodeDist<headDist:
        node.link=head
        last=head
        while last.link!=head:
            last=last.link
        last.link=head
        head=node
        return
    
    current=head
    while current.link!=head:
        pre=current
        current=current.link
        currX,currY=current.data[1:]
        currDist=math.sqrt(currX**2+currY**2)
        if currDist>nodeDist:
            pre.link=node
            node.link=current
            return
    
    current.link=node
    node.link=head

memory=[]
head, current,pre=None,None,None


if __name__=="__main__":
    dataArray=[]
    for i in range(65,75):
        x=random.randint(1,100)
        y=random.randint(1,100)
        storeName=chr(i)
        dataArray.append([storeName,x,y])
    
    for data in dataArray:
        makeStoreList(data)

    printNodes(head)