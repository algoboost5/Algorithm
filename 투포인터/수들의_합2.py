import sys
n,m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

cnt = 0

one, two = 0 , 1

tmp = arr[one]
while one < n:
    if tmp == m:
        cnt += 1
        tmp -= arr[one]
        one += 1

    if two == n and tmp < m:
        break

    elif tmp < m:
        tmp += arr[two]
        two += 1

    elif tmp > m:
        tmp -= arr[one]
        one += 1

print(cnt)