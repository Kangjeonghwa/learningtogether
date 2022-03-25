#플로이드워셜 알고리즘 사용
n, m=map(int, input().split())

INF = int(1e9)
graph=[[INF]*(n+1) for _ in range(n+1)] #n * n 그래프 생성

for a in range(1, n + 1) :
  for b in range(1, n + 1) :
    if a == b :
      graph[a][b] = 0 #시작-도착이 같은 경우 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1   #양방향이므로 a-b,b-a 모두 1로 설정

x, k = map(int, input().split())

for c in range(1, n + 1) :
  for a in range(1, n + 1) :
    for b in range(1, n + 1) :
      graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])
      # Dab = min(Dab, Dak+Dkb)

distance = graph[1][k] + graph[k][x]
#1부터 k로 가는 최단거리 + k부터 x로 가는 최단거리

if distance >= INF :
  print("-1")
else :
  print(distance)