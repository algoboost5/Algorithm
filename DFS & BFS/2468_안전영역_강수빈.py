import sys

def bfs(sea_map, visited, cur, w, h ):
    direcs = [[0, -1], [-1,0], [1,0],  [0, 1]]
    stack = [cur]

    while stack:

        cur_x, cur_y = stack[0]
        del stack[0]
        # print(cur_x, cur_y)
        for direc in direcs:
            next = (cur_x+direc[0], cur_y+direc[1])
            if next[0]>=0 and next[0]<w and next[1]>=0 and next[1]<h and sea_map[next[1]][next[0]] and not visited[next[1]][next[0]]:
                visited[next[1]][next[0]] = True
                stack.append(next)
    return visited


def cnt_island(sea_map, w, h) :
    visited = [[False]*w for _ in range(h)]
    cnt = 0
    for w_idx in range(w):
        for h_idx in range(h):
            if sea_map[h_idx][w_idx] and not visited[h_idx][w_idx]:
                cnt+=1
                visited[h_idx][w_idx] = True
                visited = bfs(sea_map, visited, (w_idx, h_idx), w, h)
                # print(visited)
    return cnt

n = int(sys.stdin.readline())
land_map = []
max_val = 0
min_val = 101
for _ in range(n):
    land_map.append(list(map(int, sys.stdin.readline().split())))
    max_val = max(max_val, max(land_map[-1]))
    min_val = min(min_val, min(land_map[-1]))

max_island = 0
for water in range(min_val-1, max_val+1):
    water_map = [[False]*n for _ in range(n)]
    for h_idx in range(n):
        for w_idx in range(n):
            water_map[h_idx][w_idx] = land_map[h_idx][w_idx]>water
    cnt = cnt_island(water_map, n, n)
    max_island= max(max_island, cnt)


print(max_island)
#
# sea_map = [[0] * w for _ in range(h)]
# for h_idx in range(h):
#     line = list(map(int, sys.stdin.readline().split()))
#     for w_idx, ele in enumerate(line):
#         sea_map[h_idx][w_idx] = ele
#
# print(cnt_island(sea_map, w, h))

# w, h = 100, 100
#
# sea_map = [[1] * w for _ in range(h)]
# print(cnt_island(sea_map, w, h))



