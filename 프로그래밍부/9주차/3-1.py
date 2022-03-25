import sys
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]


#같은 연합을 이루는 나라들을 구한다.
def bfs(i,j):
    visited[i][j] = 1 #방문처리
    q = deque()
    q.append([i,j])
    temp= [] #현재 노드로부터 연합될 노드들이 담길 리스트
    temp.append([i,j])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            #이동가능하고 아직 방문전이면
            if 0<=nx<N and 0<= ny < N and visited[nx][ny]==0:
                #조건에 부합하면
                if L <= abs(graph[nx][ny]-graph[x][y]) <= R:
                    visited[nx][ny] = 1 #방문처리
                    q.append([nx,ny])
                    temp.append([nx,ny])
    return temp #연합이 되는 한덩이

cnt = 0
while True:
    visited = [[0] * N for _ in range(N)]
    flag= False #전체를 돌기전에 False로 맞춰주고 인구이동이 일어났따면 True로 바꿈
    for i in range(N):
        for j in range(N):
            #아직 방문전이면 해당노드를 시작으로하는 bfs호출
            if visited[i][j] == 0:
                temp = bfs(i,j)
                print(temp)
                if len(temp) >1: # 누군가와 연합이 되었다면 --> 인구이동
                    flag=True
                    print(temp)
                    num = sum(graph[x][y] for x,y in temp)//len(temp)
                    for x,y in temp:
                        graph[x][y] = num
    if flag == False: #인구이동이 한번도 없었다면 더이상 진행x -> break
        break
    cnt += 1 #이동이 일어났을때만 +1

print(cnt) #전체를 확인했을때 이동이 일어난 횟수 (서로 떨어진 칸에서 인구이동이 각각 일어났어도 한번의 전체턴이면 하나로친다)