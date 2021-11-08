from itertools import *

N,S = map(int,input().split())
num_list = list(map(int,input().split()))

answer = 0

for i in range(1,N+1):
    for c in combinations(num_list,i):
        if S == sum(c):
            answer += 1

print(answer)