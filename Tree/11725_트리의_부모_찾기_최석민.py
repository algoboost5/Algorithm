from collections import deque

def bfs(v):
    q= deque([v])
    visited[v]= 1

    while q:
        x= q.popleft()

        for i in adj[x]:
            if not visited[i]:
                q.append(i)
                visited[i]= x


n= int(input())
adj= [[] for _ in range(n+1)]
visited= [0]* (n+1)
for i in range(n-1):
    a, b= map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [0] * (n + 1)
bfs(1, 1)

for i in range(2, n+1):
    print(visited[i])