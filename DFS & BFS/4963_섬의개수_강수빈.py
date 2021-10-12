import sys

def bfs(sea_map, visited, cur, w, h ):

    direcs = [[-1, -1], [0, -1], [1, -1], [-1,0], [1,0], [-1, 1], [0, 1], [1, 1]]
    stack = [cur]
    while stack:
        cur_x, cur_y = stack[0]
        del stack[0]

        for direc in direcs:
            next = (cur_x+direc[0], cur_y+direc[1])

            if next[0]>=0 and next[0]<w and next[1]>=0 and next[1]<h and sea_map[next[1]][next[0]] == 1 and visited[next[1]][next[0]]!=1:
                visited[next[1]][next[0]] = 1
                stack.append(next)



    return visited



def cnt_island(sea_map, w, h) :
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for w_idx in range(w):
        for h_idx in range(h):
            if sea_map[h_idx][w_idx]==1 and visited[h_idx][w_idx]!=1:
                cnt+=1
                visited[h_idx][w_idx] = 1
                visited = bfs(sea_map, visited, (w_idx, h_idx), w, h)

    return cnt

while (True):
    w, h = map(int, sys.stdin.readline().split())
    if w==0: break

    sea_map = [[0] * w for _ in range(h)]
    for h_idx in range(h):
        line = list(map(int, sys.stdin.readline().split()))
        for w_idx, ele in enumerate(line):
            sea_map[h_idx][w_idx] = ele

    print(cnt_island(sea_map, w, h))

# w, h = 100, 100
#
# sea_map = [[1] * w for _ in range(h)]
# print(cnt_island(sea_map, w, h))



