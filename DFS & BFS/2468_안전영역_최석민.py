
# 높이를 전체적으로 내가 탐색하는 느낌인 것 같다..
# bfs로 간단하게 풀면 될 듯.. 전 좌표에서.. 방문을 하지 않았고.. 범위 내에 있는 애들

from collections import deque

moves= [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(v):
    q= deque([v])
    visited[v[0]][v[1]]= 1

    while q:
        x, y= q.popleft()

        for dx, dy in moves:
            tx, ty= x+ dx, y+ dy
            if 0<= tx< n and 0<= ty< n:
                if not visited[tx][ty] and adj[tx][ty] > depth:
                    q.append([tx, ty])
                    visited[tx][ty]= 1

        # 굳이 따로 종료조건이 필요할 것 같지는 않음


n= int(input())
adj= [list(map(int, input().split())) for _ in range(n)]

# 일단 max depth를 탐색해서 그만큼동안 반복문을 돌아야 하지 않겠는가 ?
max_depth= adj[0][0]
for i in range(n):
    max_depth= max(max_depth, max(adj[i]))

max_cnt= 0

for depth in range(max_depth):
    cnt= 0
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and adj[i][j] > depth:
                bfs([i, j])
                cnt+=1
    max_cnt= max(max_cnt, cnt)
print(max_cnt)

