import sys
n = int(sys.stdin.readline())

n_list = list(map(int, sys.stdin.readline().split()))

n_list.sort(reverse=True)
    
sum = 0
score = 0
total = 0

for i in range(0,n-1):
    score = n_list[i] * n_list[i+1]
    n_list[i+1] = n_list[i] + n_list[i+1]
    total = total + score
    
print(total)