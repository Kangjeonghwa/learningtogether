from collections import deque

N, M, K, X = map(int, input().split(' '))

path = [[False] * (N+1) for _ in range(N+1)]
distance=[-1]*(N+1)
distance[X]=0

for i in range(M):
    x, y = map(int, input().split(' '))
    path[x][y]=True

q=deque([X])

while q:
    head=q.popleft()
    for i in range(M+1):
        if path[head][i]:
            if distance[i]==-1:
                distance[i]=distance[head]+1
                q.append(i)

for i in range(N+1):
    if distance[i]==K:
        print(i)

if K not in distance:
    print(-1)