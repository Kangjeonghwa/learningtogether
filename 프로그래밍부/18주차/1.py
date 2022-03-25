#크루스칼 알고리즘
def find_parent(parent, x):
    if parent[x] != x:
        parent[x]= find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v, e=map(int, input().split())  #노드 수와 간선 수 입력
parent=[0]*(v+1)    

edges=[]    #간선 리스트
max=0   #모든 간선 비용
min=0   #최소 간선 비용

# 초기화
for i in range(1,v+1):
    parent[i]=i

#간선 입력
for i in range(e):
    a, b, cost = map(int,input().split())
    edges.append((cost, a, b))

edges.sort()    #크루스칼 알고리즘을 위한 간선 비용순 정렬

for edge in edges:
    cost, a, b=edge

    if find_parent(parent,a)!=find_parent(parent,b):    #간선이 연결되어 있는지
        union_parent(parent,a,b)    #연결되어있지 않다면 연결(집합에 포함)하고 최솟값에 간선더함
        min+=cost
    
    max+=cost

#print("최대금액: %d"%max)
#print("최소금액: %d"%min)
print("절약금액: %d"%(max-min)) #최대-최소