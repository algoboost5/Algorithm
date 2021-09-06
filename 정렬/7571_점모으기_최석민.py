import math

n, m= map(int, input().split())
x, y= [], []

for i in range(m):
    tx, ty= map(int, input().split())
    x.append(tx)
    y.append(ty)

x.sort()
y.sort()

dx, dy= x[m//2], y[m//2]
result= 0

for i in range(m):
    result+= abs(x[i]- dx) + abs(y[i]- dy)

print(result)
