#플로이드워셜 알고리즘 사용
n, m=map(int, input().split())

INF = int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n + 1) :
  for b in range(1, n + 1) :
    if a == b :
      graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1     #양방향


for c in range(1, n + 1) :
  for a in range(1, n + 1) :
    for b in range(1, n + 1) :
      graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])
      # Dab = min(Dab, Dak+Dkb)

max_node = 0
max_dist = 0
max_node_lst = []

for i in range(1,n+1):
    if max_dist<graph[1][i]:    #시작이 1이므로 그래프의 1행만
        if graph[1][i]==INF:
            continue
        max_node = i
        max_dist = graph[1][i]
        max_node_lst = [max_node]
    elif max_dist == graph[1][i]:
        max_node_lst.append(i)

print(max_node, max_dist, len(max_node_lst))