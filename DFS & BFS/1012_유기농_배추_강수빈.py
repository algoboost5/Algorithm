
import sys
from collections import deque


def out_boundary(coord, w, h):
    if(coord[0]>=w or coord[0]<0):
        return True
    if(coord[1]>=h or coord[1]<0):
        return True

    return False

def bfs(cur, w, h, visited, cabb_map) :

    area = 1

    #up, down, left, right
    dirs = [(0,-1), (0,1), (-1,0), (1,0)]
    cabb_stack = deque([])
    cabb_stack.append(cur)
    visited[cur[0]][cur[1]] = 1

    while(len(cabb_stack)!=0):
        cur = cabb_stack.pop()
        for dir in dirs:
            m_coord = (cur[0]+dir[0], cur[1]+dir[1])
            print(m_coord)
            if not out_boundary(m_coord, w, h) and visited[m_coord[0]][m_coord[1]]==0 and cabb_map[m_coord[0]][m_coord[1]]==1:
                cabb_stack.append(m_coord)
                visited[m_coord[0]][m_coord[1]] = 1

    return visited

testcases = int(sys.stdin.readline())
for case in range(testcases):
    width, height, cabb_num = map(int, sys.stdin.readline().split())
    cabb_map = []
    visited = []
    cnt = 0
    for w in range(width):
        map_row = []
        visit_row = []
        for h in range(height):
            map_row.append(0)
            visit_row.append(0)
        cabb_map.append(map_row)
        visited.append(visit_row)


    for cabb in range(cabb_num):
        w, h = map(int, sys.stdin.readline().split())
        cabb_map[w][h] = 1



    for w in range(width):
        for h in range(height):
            # print((w,h), cabb_map[w][h], visited[w][h])
            if cabb_map[w][h]==1 and visited[w][h]==0:

                visited = bfs((w,h), width, height, visited, cabb_map)
                cnt += 1

    print(cnt)




