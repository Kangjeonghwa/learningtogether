#다익스트라 알고리즘 사용
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

graph = defaultdict(list)
distances = [INF] * (N+1) #무한으로 기본거리 설정

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) #시작도시 a, 도착도시 b, 거리 c

start, end = map(int, input().split())


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))

    while queue:
        dist, now = heapq.heappop(queue)

        if distances[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if distances[node[0]] > cost:
                distances[node[0]] = cost
                heapq.heappush(queue, (cost, node[0]))


dijkstra(start)

print(distances[end])