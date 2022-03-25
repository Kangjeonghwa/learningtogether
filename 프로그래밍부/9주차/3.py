from collections import deque

n, l, r = map(int, input().split(' '))  #크기, 최소, 최대 입력
graph = [list(map(int, input().split(' '))) for _ in range(n)]  #인구 입력

d_x = [-1, 0, 1, 0] #x 방향 리스트
d_y = [0, 1, 0, -1] #y 방향 리스트

is_move = False #연합 형성 여부


def bfs(c_x, c_y, visited, grpah):
    global is_move
    people = graph[c_x][c_y]    #인구
    count = 1                   #연합 영토 수
    queue = deque()             #탐색을 위한 큐 생성
    queue.append((c_x, c_y))    
    visited[c_x][c_y] = True    #방문 처리
    temp = list()               #인구 분배를 위한 리스트 생성
    temp.append((c_x, c_y))     

    while queue:                        #큐가 빌 때까지 반복
        pop_x, pop_y = queue.popleft()  #큐에서 꺼냄

        for i in range(4):              #방향 리스트 사용을 위한 for문
            n_x = pop_x + d_x[i]        #x 방향
            n_y = pop_y + d_y[i]        #y 방향

            if n_x < 0 or n_x >= n or n_y < 0 or n_y >= n:  #범위 만족 여부
                continue

            if visited[n_x][n_y]:                           #방문 여부
                continue

            if l <= abs(grpah[pop_x][pop_y] - grpah[n_x][n_y]) <= r:    #최대최소 조건 만족 여부
                visited[n_x][n_y] = True            #방문 처리
                queue.append((n_x, n_y))            #깊이 탐색을 위한 큐 삽입
                people += graph[n_x][n_y]           #연합>>>인구 +
                count += 1                          #연합>>>영토 개수+1
                temp.append((n_x, n_y))             #인구 분배 리스트에 삽입

    move_people = people // count                   #이동하여 분배할 인구 수 계산

    if count > 1:                                   #연합 했을 경우
        is_move = True                              #연합 여부에 True
        for x, y in temp:                           
            graph[x][y] = move_people               #이동 인구 분배


answer = 0      #초기값 0으로 설정

while True:                                     #이동한 인구가 없을 때까지 반복
    is_move = False                             #반복 할 때마다 이동 여부 false로 초기화
    visited = [[False] * n for _ in range(n)]   #방문 리스트 초기화
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:               #중첩 for문과 방문 여부로 방문하지 않은 영토                     
                bfs(i, j, visited, graph)       #함수로 호출

    if is_move:
        answer += 1     #위에서 연합이 True가 되어 이동하였을 때 +1
    else:
        break           #이동이 없어 is_move가 그대로 false일 때, 반복문을 빠져나옴

print(answer)           # 몇 번 인구가 이동했는지 출력