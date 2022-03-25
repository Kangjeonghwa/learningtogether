def find_parent(parent, x):
    if parent[x] != x:
        parent[x]= find_parent(parent,parent[x])
    return parent[x]

v=int(input())
e=int(input())
answer=0
parent=[0]*(v+1)
planes=[]

for i in range(1,v+1):
    parent[i]=i

for _ in range(e):
    planes.append(int(input()))

for plane in planes:
    docking = find_parent(parent, plane)
    if docking == 0:
        break
    parent[docking] = parent[docking - 1]
    answer += 1
print(answer)