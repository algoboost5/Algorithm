import sys
import math

n,m = map(int,sys.stdin.readline().split())
x_points = []
y_points = []
for _ in range(m):
    x,y = map(int, sys.stdin.readline().split())
    x_points.append(x)
    y_points.append(y)

x_mid = sorted(x_points)[m//2]
y_mid = sorted(y_points)[m//2]
moves = 0
for idx in range(m):
    moves += abs(x_points[idx]-x_mid) + abs(y_points[idx]-y_mid)
print(moves)