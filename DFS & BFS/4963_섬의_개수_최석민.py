from collections import deque

moves= [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

def bfs(v):
    q= deque([v])
    visited[v[0]][v[1]]= 1

    while q:
        x, y= q.popleft()

        for dx, dy in moves:
            tx, ty= x+ dx, y+ dy

            if 0<= tx< h and 0<= ty< w:
                if not visited[tx][ty]:
                    if adj[tx][ty]== 1:
                        q.append([tx, ty])
                        visited[tx][ty]= 1


while True:
    w, h= map(int, input().split())
    if w==0 and h==0: break;

    adj= []
    visited=[[0]*w for _ in range(h)]
    cnt= 0
    for i in range(h):
        adj.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and adj[i][j]==1:
                bfs([i, j])
                cnt+=1
    print(cnt)

