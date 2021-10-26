import sys

n,m = map(int, sys.stdin.readline().split())
num_ls = list(map(int, sys.stdin.readline().split()))

sum_ls = [0]
for n_idx, num in enumerate(num_ls):
    sum_ls.append(sum_ls[-1]+num)
answer = 0

for start in range(1,n+1):
    left = start
    right = n
    mid = (left+right)//2
    start_sum = sum_ls[left-1]
    while left<=right:
        mid = (left+right)//2
        mid_sum = sum_ls[mid]

        if(mid_sum-start_sum>m):
            right = mid-1
        elif(mid_sum-start_sum<m):
            left = mid+1
        else:
            answer+=1
            break


print(answer)

