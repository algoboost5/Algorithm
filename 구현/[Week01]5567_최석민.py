from collections import deque

def bfs(v):
    global result
    q= deque([v])
    visited[v]= 1

    while q:
        x= q.popleft()
        if visited[x]== 3: break;
        for friend in friends[x]:
            if not visited[friend]:
                q.append(friend)
                visited[friend]= visited[x]+ 1
                result+=1

if __name__ == "__main__":
    n= int(input())
    m= int(input())
    result= 0
    friends= [[] for _ in range(n+1)]
    visited= [0]*(n+1)

    for i in range(m):
        x, y= map(int, input().split())
        friends[x].append(y)
        friends[y].append(x)

    bfs(1)
    print(result)