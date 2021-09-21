import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
sum_li = [li[0]]
# 1~i까지의 합
for i in range(1, n):
    sum_li.append(sum_li[i-1]+li[i])
for _ in range(m):
    start, end = map(int,input().split())
    if start == 1:
        print(sum_li[end-1])
    else:
        print(sum_li[end-1]-sum_li[start-2])