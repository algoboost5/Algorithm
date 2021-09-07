import sys

n = int(sys.stdin.readline())
n_list = sorted(list(map(int, sys.stdin.readline().split())))
for _ in range(n-1):
    row_list = list(map(int, sys.stdin.readline().split()))
    for col_idx in range(n):

        if row_list[col_idx] > n_list[0]:
            n_list[0] = row_list[col_idx]
            n_list.sort()


print(n_list[0])