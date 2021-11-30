# 누적 합(prefix Sum) 으로 구하기

import sys
n, m = map(int,sys.stdin.readline().split())

arr = list(map(int,sys.stdin.readline().split()))

sum_value = 0

# 누적합 리스트 생성
prefix_sum = [0]

# 앞에서부터 더해가는 리스트 생성
for y in arr:
    sum_value += y
    prefix_sum.append(sum_value)

# (j)번째까지의 합 - (i-1)번째까지의 합
for _ in range(m):
    i, j = map(int,sys.stdin.readline().split())
    print(prefix_sum[j] - prefix_sum[i-1])