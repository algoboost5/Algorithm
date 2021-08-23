import sys
from collections import deque

h, w = map(int, input().split())
matrix = [[] for _ in range(h)]

for _ in range(h):
    matrix[_] = list(map(int, input().split()))

box_n = 0
box_s = 0
stack = deque()
dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]

for i in range(h):
    for j in range(w):
        if matrix[i][j] == 1:
            stack.append([i, j])
            matrix[i][j] = 0
            box_n = box_n + 1
            box_s_tmp = 0

            while stack:
                a, b = stack.pop()
                box_s_tmp = box_s_tmp + 1
                
                for dy, dx in zip(dir_y, dir_x):
                    if a+dy < 0 or a+dy > h-1 or b+dx < 0 or b+dx > w-1:
                        continue
                    if matrix[a+dy][b+dx] == 1:
                        matrix[a+dy][b+dx] = 0
                        stack.append([a+dy, b+dx])

            box_s = max(box_s, box_s_tmp)

print(box_n)
print(box_s)


