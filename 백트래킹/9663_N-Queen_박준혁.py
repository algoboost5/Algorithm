import sys

# 해당 위치에 퀸이 존재할 수 있는지 확인, 가능하면 다음 퀸의 위치 탐색

n = int(sys.stdin.readline())
board = [0] * n
count = 0
visited = [False] * n

def exist(x):
    for i in range(x):
        if abs(board[x] - board[i]) == x - i:
            return False
    return True

def n_queen(x):
    global count
    if x == n:
        count += 1
        return

    for i in range(n):
        if visited[i]:
            continue
        
        board[x] = i
        if exist(x):
            visited[i] = True
            n_queen(x+1)
            visited[i] = False

n_queen(0)
print(count)