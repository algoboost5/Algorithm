from collections import deque

moves= [[-1, 0], [0, -1], [0, 1], [1, 0]] # 위, 왼, 오, 아 순서

def bfs(v):
    q= deque([v])
    visited[v[0]][v[1]]= 1


    while q:
        x, y, sh, cnt= q.popleft()

        for dx, dy in moves:
            tx, ty= x+ dx, y+ dy

            if 0<= tx< n and 0<= ty< n:
                if not visited[tx][ty]:
                    if board[tx][ty] == 0 or board[tx][ty] == sh:
                        q.append([tx, ty, sh, cnt])
                        visited[tx][ty] = visited[x][y] +1
                    elif board[tx][ty] < sh:
                        board[tx][ty]= 0
                        visited[tx][ty] = visited[x][y]
                        if cnt== sh-1:
                            return tx, ty, sh+1, 0
                        else:
                            return tx, ty, sh, cnt+1
    return 0, 0, 0, 0


n= int(input())
board= [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j]== 9:
            shark= [i, j]; break;

res= 0
X, Y, SHARK, CNT= shark[0], shark[1], 2, 0
board[X][Y]= 0
for i in range(50):
    visited = [[0] * n for _ in range(n)]
    X, Y, SHARK, CNT= bfs([X, Y, SHARK, CNT])
    
    res+= visited[X][Y]
    if [X, Y, SHARK, CNT]== [0, 0, 0, 0]:
        break;
    # print(X, Y, SHARK, CNT, visited[X][Y])
    # for j in board:
    #     print(j)
    # print()

print(res)
