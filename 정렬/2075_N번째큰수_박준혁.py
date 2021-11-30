import sys
n = int(sys.stdin.readline().strip())
n_list = []

for i in range(n):
    n_list += [int(n) for n in sys.stdin.readline().split()]
    n_list = (sorted(n_list, reverse=True))[:n]
print(n_list[-1])