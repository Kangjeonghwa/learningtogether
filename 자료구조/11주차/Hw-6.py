# 교과서 357 페이지 응용예제 2

class Graph():
    def __init__ (self,size):
        self.SIZE=size
        self.graph=[[0 for _ in range(size)] for _ in range(size)]

def printGraph(g):
    print('  ',end=' ')
    for v in range(g.SIZE):
        print(cityAry[v],end=' ')
    print()
    for row in range(g.SIZE):
        print(cityAry[row],end='  ')
        for col in range(g.SIZE):
            print("%2d" %g.graph[row][col],end='    ')
        print()
    print()

def findVertex(g,findVtx):
    stack=[]
    visitedAry=[]

    current=0
    stack.append(current)
    visitedAry.append(current)

    while (len(stack)!=0):
        next=None
        for vertex in range(gSize):
            if g.graph[current][vertex]!=0:
                if vertex in visitedAry:
                    pass
                else:
                    next=vertex
                    break
        
        if next!=None:
            current=next
            stack.append(current)
            visitedAry.append(current)
        else:
            current=stack.pop()

    if findVtx in visitedAry:
        return True
    else:
        return False

G1=None
cityAry=['서울','뉴욕','런던','북경','방콕','파리']
서울,뉴욕,런던,북경,방콕,파리=0,1,2,3,4,5

gSize=6
G1=Graph(gSize)
G1.graph[0][1]=80;G1.graph[0][3]=10
G1.graph[1][0]=80;G1.graph[1][3]=40;G1.graph[1][4]=70
G1.graph[2][4]=30;G1.graph[2][5]=60
G1.graph[3][0]=10;G1.graph[3][1]=40;G1.graph[3][4]=50
G1.graph[4][1]=70;G1.graph[4][3]=50;G1.graph[4][2]=30;G1.graph[4][5]=20
G1.graph[5][4]=20;G1.graph[5][2]=60

print('## 해저 케이블 연결을 위한 전체 연결도 ##')
printGraph(G1)

edgeAry=[]
for i in range(gSize):
    for k in range(gSize):
        if G1.graph[i][k]!=0:
            edgeAry.append([G1.graph[i][k],i,k])

from operator import itemgetter
edgeAry=sorted(edgeAry,key=itemgetter(0),reverse=False)

newAry=[]
for i in range(0,len(edgeAry),2):
    newAry.append(edgeAry[i])

index=0
while(len(newAry)>gSize-1):
    start=newAry[index][1]
    end=newAry[index][2]
    saveCost=newAry[index][0]

    G1.graph[start][end]=0
    G1.graph[end][start]=0

    startYN=findVertex(G1, start)
    endYN=findVertex(G1, end)

    if startYN and endYN:
        del(newAry[index])
    else:
        G1.graph[start][end]=saveCost
        G1.graph[end][start]=saveCost
        index+=1

print('## 가장 효율적인 해저 케이블 연결도 ##')
printGraph(G1)