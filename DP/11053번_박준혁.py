n = int(input())

arr = list(map(int,input().split()))

D = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            D[i] = max(D[i], D[j]+1)

print(max(D))

# 이렇게 푸는게 맞는건가..?
