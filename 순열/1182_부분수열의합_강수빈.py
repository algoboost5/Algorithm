import sys
from itertools import *

if __name__=="__main__":
    n, s = map(int, sys.stdin.readline().split())
    n_ls = list(map(int, sys.stdin.readline().split()))

    cnt = 0
    for num in range(1, n+1):
        for com in combinations(n_ls, num):
            if sum(com)==s:
                cnt+=1

    print(cnt)