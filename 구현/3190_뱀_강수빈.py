import sys

N = int(sys.stdin.readline())
A = int(sys.stdin.readline())
# apple map init
a_map = [[0]*N for _ in range(N)]
for _ in range(A):
    r, c = map(int, sys.stdin.readline().split())
    a_map[r-1][c-1] = 2

# snake direc chg init
L = int(sys.stdin.readline())
direc_chg = {}
for _ in range(L):
    t, c = sys.stdin.readline().split()
    t = int(t)
    c = 1 if c=='D' else -1
    direc_chg[t] = c


# 뱀이 있을 경우 1, 사과 있을 경우 2, 아무것도 없을 경우 0
# left_apple = A
a_map[0][0] = 1
time = 0
# row, col 순서, 오른쪽으로 회전
direcs = [(0,1), (1, 0), (0,-1), (-1, 0)]
direc = 0
snake = [(0,0)]

while(True):
    time += 1
    next_coord = (snake[-1][0]+direcs[direc][0], snake[-1][1]+direcs[direc][1])
    # out of boundary
    if(next_coord[0]>=N or next_coord[0]<0 or next_coord[1]>=N or next_coord[1]<0):
        break
    # no apple
    if(a_map[next_coord[0]][next_coord[1]] == 0) :
        snake.append(next_coord)
        a_map[snake[-1][0]][snake[-1][1]] = 1
        a_map[snake[0][0]][snake[0][1]] = 0
        del snake[0]
    # meet snake
    elif (a_map[next_coord[0]][next_coord[1]] == 1):
        break
    # meet apple
    else :
        snake.append(next_coord)
        a_map[snake[-1][0]][snake[-1][1]] = 0
    # direction chg
    if time in direc_chg.keys():
        direc = (direc + direc_chg[time]) % 4



print(time)