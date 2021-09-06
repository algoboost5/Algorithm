import sys
# input = sys.stdin.readline
input_n= int(input())
li = list(map(int,input().split()))
for _ in range(input_n-1):
    li+= list(map(int,input().split()))
    li = sorted(li,reverse=True)[:input_n]
print(li[-1])
