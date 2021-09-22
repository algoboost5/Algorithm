import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int,input().split()))
result = [1]*n

for i in range(n):
    for j in range(i):
        if li[i]>li[j]:
            # li[i]보다 작은 수는 여러개 있을 수 있음
            # 그것들 중 가장 긴 수열을 찾아내야하니까 다 돌면서 가장 긴 길이 찾음
            result[i] = max(result[i],result[j]+1) # [j]에 +1하는건 자기자신
print(max(result))