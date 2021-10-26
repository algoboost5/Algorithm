import sys


n, m, r = map(int, sys.stdin.readline().split())
n_section = min(n//2, m//2)

num_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result_map = [[0]*m for _ in range(n)]


for idx in range(n_section):
    cur = [idx, idx]
    section_coord=[cur]
    section_num = [num_map[cur[0]][cur[1]]]
    h = m-2*idx
    w = n-2*idx

    # go_down
    for _ in range(1,h):
        cur = cur.copy()
        cur[1] += 1
        section_coord.append(cur)
        section_num.append(num_map[cur[0]][cur[1]])
    # go right
    for _ in range(1,w):
        cur = cur.copy()
        cur[0] += 1
        section_coord.append(cur)
        section_num.append(num_map[cur[0]][cur[1]])
    # go up
    for _ in range(1,h):
        cur = cur.copy()
        cur[1] -= 1
        section_coord.append(cur)
        section_num.append(num_map[cur[0]][cur[1]])
    # go left
    for _ in range(1,w-1):
        cur = cur.copy()
        cur[0] -= 1
        section_coord.append(cur)
        section_num.append(num_map[cur[0]][cur[1]])

    # rotate section
    for _ in range(r):
        tmp = section_num[0]
        del section_num[0]
        section_num.append(tmp)

    for n_idx, num in enumerate(section_num):
        cx, cy = section_coord[n_idx]
        result_map[cx][cy] = num

for line in result_map:
    print(' '.join(map(str, line)))

