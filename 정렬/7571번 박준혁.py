import math
import sys

a, b= map(int, sys.stdin.readline().split())
x_list = []
y_list = []

for i in range(b):
    x, y= map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)

x_list.sort()
y_list.sort()

x, y= x_list[b//2], y_list[b//2]
answer= 0

for i in range(b):
    answer += abs(x_list[i]- x)
    answer += abs(y_list[i]- y)

print(answer)