import sys
import statistics
f = sys.stdin.readline

N, M = map(int, f().split())
y_list = []
x_list = []
y_sum, x_sum = 0, 0

for i in range(M):
    y, x = map(int, f().split())
    y_list.append(y)
    x_list.append(x)
    y_sum += y
    x_sum += x

y_mean = round(y_sum / M)
x_mean = round(x_sum / M)

print(y_mean, x_mean)

dist = 0
for y, x in zip(y_list, x_list):
    dist += abs(y-y_mean) + abs(x-x_mean)

print(dist)
