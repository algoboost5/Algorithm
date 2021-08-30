import sys
from collections import deque

slime_num = int(sys.stdin.readline())
slimes = deque(sorted(list(map(int, sys.stdin.readline().split()))))

score=0
while len(slimes)>1:
    top1 = slimes.pop()
    top2 = slimes.pop()

    slimes.append(top1+top2)
    score+=top1*top2

print(score)