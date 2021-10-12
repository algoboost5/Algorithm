import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0] * n for _ in range(n)]
visit = [0] * n
answer = 0

def bfs(num):
    k = [num]
    while k:
        a = k.pop(0)
        for i in range(n):
            if arr[a][i] == 1 and visit[i] == 0:
                k.append(i)
                visit[i] = 1
       
for i in range(m):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 1
    arr[y - 1][x - 1] = 1

for i in range(len(visit)):
    if visit[i] == 0:
        bfs(i)
        answer += 1
        
print(answer)