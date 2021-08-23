import sys
from collections import deque


def out_boundary(coord, h, w):
    if coord[0]>=h or coord[0]<0:
        return True
    if coord[1]>=w or coord[1]<0:
        return True
    return False

def dfs(img_map, cur, visited, h, w):
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    area=1

    for dir in dirs:
        m_coord = (cur[0] + dir[0], cur[1] + dir[1])
        if (not out_boundary(m_coord, h, w)) and img_map[m_coord[0]][m_coord[1]] == 1 and visited[m_coord[0]][m_coord[1]] == 0:
            visited[m_coord[0]][m_coord[1]] = 1
            area_plus, visited = dfs(img_map, m_coord, visited, h, w)
            area += area_plus

    return area, visited

def bfs(img_map, cur, visited, h, w):
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    area = 1

    coord_stack = deque([])
    coord_stack.append(cur)


    while(len(coord_stack) !=0):
        cur = coord_stack.pop()
        for dir in dirs:
            m_coord = (cur[0] + dir[0], cur[1] + dir[1])
            if(not out_boundary(m_coord, h, w)) and img_map[m_coord[0]][m_coord[1]] == 1 and visited[m_coord[0]][m_coord[1]]==0:
                visited[m_coord[0]][m_coord[1]] = 1
                coord_stack.append(m_coord)
                area += 1

    return area, visited



height, width = map(int, sys.stdin.readline().split())
img_map = []
visited = []

for h in range(height):
    img_map.append(list(map(int, sys.stdin.readline().split())))
    visit_row = []
    for w in range(width):
        visit_row.append(0)
    visited.append(visit_row)


cnt = 0
max_area = 0
for h in range(height):
    for w in range(width):
        if(img_map[h][w] ==1 and visited[h][w] == 0):
            visited[h][w] = 1
            area,visited = bfs(img_map, (h,w), visited, height, width)
            max_area = max(max_area, area)
            cnt += 1

print(cnt)
print(max_area)