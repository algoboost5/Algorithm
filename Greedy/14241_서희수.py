import sys
# input = sys.stdin.readline

input_n= int(input())
slime = list(map(int,input().split()))

slime.sort()
result = 0
merge_slime = slime[0]
for i in slime[1:]:
    result += merge_slime*i
    merge_slime+=i

print(result)
