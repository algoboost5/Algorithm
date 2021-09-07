
# 일단 리스트에 input의 모든 값을 넣으니 메모리 초과가 났다..
# 한 줄을 입력 받을 때마다 주기적으로 필요없는 것은 지워줘야 하는 느낌..
# 이 때 최소, 최대 힙 자료구조를 떠올려야 함 -> 최대, 최소 값을 빠르게 찾는 자료구조

import heapq

n= int(input())
heap= []

# 처음 N개의 값을 heap에 넣어줌
nums = list(map(int, input().split()))
for num in nums:
    heapq.heappush(heap, num)

for i in range(n-1):
    nums= list(map(int, input().split()))
    for num in nums:
        heapq.heappush(heap, num)
        heapq.heappop(heap)

print(heap[-n])

