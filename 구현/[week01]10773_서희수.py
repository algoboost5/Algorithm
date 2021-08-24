
import sys
n = int(sys.stdin.readline())
result = []

for _ in range(n):
    i = int(sys.stdin.readline())
    if i != 0:
        result.append(i)
    else:
        result.pop()

print(sum(result))
