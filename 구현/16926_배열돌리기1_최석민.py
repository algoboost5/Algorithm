

n, m, r= map(int, input().split())

directions= ['D', 'R', 'U', 'L']
board= [list(map(int, input().split())) for _ in range(n)]

depth= int(min(n, m)//2)
for _ in range(r):
    for dep in range(depth):
        x, y= dep, dep
        tmp= board[x][y]
        for dir in directions:
            if dir== 'D':
                for i in range(n-1-2*dep):
                    x+=1
                    tmp2= board[x][y]
                    board[x][y]= tmp
                    tmp= tmp2

            elif dir=='R':
                for i in range(m-1-2*dep):
                    y+=1
                    tmp2= board[x][y]
                    board[x][y]= tmp
                    tmp= tmp2

            elif dir=='U':
                for i in range(n-1-2*dep):
                    x-=1
                    tmp2 = board[x][y]
                    board[x][y] = tmp
                    tmp = tmp2

            elif dir=='L':
                for i in range(m-1-2*dep):
                    y-=1
                    tmp2= board[x][y]
                    board[x][y]= tmp
                    tmp= tmp2

for i in range(n):
    for j in range(m):
        print(board[i][j], end=' ')
    print()

