from collections import deque

move= [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(v):
    q= deque([v])
    visited[v[0]][v[1]]= 1
    tmp_size= 0
    while q:
        x, y= q.popleft()

        for dx, dy in move:
            tx, ty= x+ dx, y+ dy
            if 0<= tx< n and 0<= ty< m:
                if not visited[tx][ty] and board[tx][ty]== 1:
                    q.append([tx, ty])
                    visited[tx][ty]= visited[x][y]+ 1
                    tmp_size+=1

    return tmp_size+1

cnt, max_size= 0, 0
n, m= map(int, input().split())
board= [list(map(int, input().split())) for _ in range(n)]
visited= [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j]== 1 and not visited[i][j]:
            tmp= bfs([i, j])
            cnt+=1
            max_size= max(max_size, tmp)

print(cnt)
print(max_size)