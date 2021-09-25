# pypy3로 해야 시간초과 안 뜸
from collections import deque
import sys
input = sys.stdin.readline

def bfs(A,B):
    q = deque()
    q.append([A,""])
    visited[A] = 1
    while q:
        x, y = q.popleft()
        D = x*2 % 10000
        if D == B: return y +"D"
        if not visited[D]:
            visited[D] = 1
            q.append([D, y + 'D'])
        S = x - 1 if x != 0 else 9999
        if S == B: return y +"S"
        if not visited[S]:
            visited[S] = 1
            q.append([S, y + 'S'])
        L = x % 1000 * 10 + x // 1000
        if L == B: return y +"L"
        if not visited[L]:
            visited[L] = 1
            q.append([L, y + 'L'])            
        R = x % 10 * 1000 + x // 10
        if R == B: return y +"R"
        if not visited[R]:
            visited[R] = 1
            q.append([R, y + 'R'])

n = int(input())    
for _ in range(n):
    A, B = map(int, input().split())
    visited = [0] * 10000
    print(bfs(A,B))