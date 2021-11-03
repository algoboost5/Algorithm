def bfs (water_map, cur, w, h, scale, fish):
    inix, iniy = cur
    # left, right, up, down
    visited = [[False]*h for _ in range(w)]
    direc = [[0, 1], [-1,0], [0,-1], [1 ,0]]

    c_stack = [(cur,0)]

    eat_fish = []
    min_step = float('inf')
    while c_stack:
        cx, cy = c_stack[0][0]
        step = c_stack[0][1]
        if(step>=min_step):
            break
        del c_stack[0]
        visited[cy][cx] = True

        for dx, dy in direc:
            # 이동할 수 있는 좌표인 경우
            if(cx+dx>=0 and cx+dx<w and cy+dy>=0 and cy+dy<h and water_map[cy+dy][cx+dx]<=int(scale) and not visited[cy+dy][cx+dx]):
                # 먹을 수 있으면
                if int(scale) > water_map[cy+dy][cx+dx] and water_map[cy+dy][cx+dx]!=0:
                    visited[cy + dy][cx + dx] = True
                    eat_fish.append(([cy + dy, cx + dx], step + 1))
                    min_step = step+1
                else:
                    visited[cy+dy][cx+dx] = True
                    c_stack.append(([cx+dx, cy+dy], step+1))

    if(eat_fish):
        eat_fish.sort()

        cy, cx = eat_fish[0][0]
        step = eat_fish[0][1]

        fish+=1
        if(fish == scale):
            scale+=1
            fish = 0

        water_map[cy][cx] = scale
        water_map[iniy][inix] = 0
        cur = [cx, cy]

        return water_map, cur, scale, fish, step

    else:
        return water_map, cur, scale, fish, 0



import sys
if __name__=="__main__":
    n = int(sys.stdin.readline())

    water_map = []
    cur = None
    for y in range(n):
        line= list(map(int, sys.stdin.readline().split()))
        for x, v in enumerate(line):
            if(v==9):
              cur = [x, y]
        water_map.append(line)

    # water_map, cur, w, h, scale
    time=0
    fish=0
    scale = 2
    while True:
        water_map, cur, scale, fish, step = bfs(water_map, cur, n, n, scale, fish)
        if step!=0:
            time+=step
        else:
            break

    print(time)