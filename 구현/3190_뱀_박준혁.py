def solution():
    time = 0
    # 동서남북 방향 지정
    snake_array = []
    direction = {0:(1,0),1:(-1,0), 2:(0,-1), 3:(0,1)}
    dir = 0

    # empty - 0, apple - 1, snake - 2
    nx, ny = 0,0
    board[0][0] = 2
    snake_array.append([0,0])

    # 끝날때까지 반복
    while(1):
        time += 1
        nx = nx + direction[dir][0]
        ny = ny + direction[dir][1]

        if not 0 <= nx < N or not 0 <= ny < N:
            break

        # apple

        if board[nx][ny] == 1:
            board[nx][ny] = 2 # moving head
            snake_array.append([nx,ny])

        # empty
        elif board[nx][ny] == 0:
            board[nx][ny] = 2
            snake_array.append([nx,ny])
            del_x, del_y = snake_array.pop(0)
            board[del_x][del_y] = 0

        # snake 
        elif board[nx][ny] == 2:
            break

        if len(snake_dir) != 0 and time == snake_dir[0][0]:
                time, new_dir = snake_dir.pop(0)
                if new_dir == 'L': # 왼쪽
                    dir = (dir + 3) % 4
                elif new_dir == 'D':
                    dir = (dir + 1) % 4

    return time

# 오른쪽/ 왼쪽 방향 바꾸는 건 % 연산자 이용하여 쉽게 할 수 있음
# 왼쪽으로 돌리기 = (현재 방향 + 3) % 4
# 오른쪽으로 돌리기 = (현재 방향 + 1) % 4
# board
N = int(input())
board = [[0 for i in range(N)] for j in range(N)]

# apple 넣기
k = int(input())
apple_locs = []
for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

# snake 시간, 방향
l = int(input())
# (sec, c(left) or d(right))
snake_dir = list(map(lambda x:[int(x[0]),str(x[1])],\
                     [input().split() for _ in range(l)])) 
print(Solution())