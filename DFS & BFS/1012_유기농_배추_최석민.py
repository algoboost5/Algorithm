import sys
sys.setrecursionlimit(10000)

move= [[1, 0], [0, 1], [-1, 0], [0, -1]]

def dfs(v):
    x, y= v[0], v[1]

    for dx, dy in move:
        tx, ty= x+ dx, y+ dy
        if 0<= tx< n and 0<= ty< m:
            if not visited[tx][ty] and adj[tx][ty]:
                visited[tx][ty]= 1
                dfs([tx, ty])

test_case= int(input())
for t in range(test_case):
    m, n, k= map(int, input().split())
    result= 0
    adj=[[0]* m for _ in range(n)]
    visited= [[0]* m for _ in range(n)]

    for _ in range(k):
        y, x= map(int, input().split())
        adj[x][y]= 1

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and adj[i][j]:
                visited[i][j]= 1
                dfs([i, j])
                result+=1
    print(result)
