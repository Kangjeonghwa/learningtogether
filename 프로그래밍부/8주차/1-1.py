n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))  # cf. str은 iterable

dx=[1,0,-1,0]
dy=[0,-1,0,1]

visited=[]

def dfs(x, y):
    # 범위 검사
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        if not((x,y) in visited):
            visited.append((x,y))
            for i in range(4):
                dfs(x+dx[i],y+dy[i])
            return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if not((i,j) in visited):
            if dfs(i, j) == True:
                result += 1

print(result)
