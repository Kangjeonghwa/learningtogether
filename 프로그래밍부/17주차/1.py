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
    

v, e = map(int,input().split())
parent=[0]*(v+1)
team=[]

for i in range(1,v+1):
    parent[i]=i

for i in range(e):
    c, a, b = map(int,input().split())
    if c==0:
        union_parent(parent,a,b)
    else:
        x=find_parent(parent,a)
        y=find_parent(parent,b)
        if x==y:
            team.append("YES")
        else:
            team.append("NO")

for NY in team:
    print(NY)