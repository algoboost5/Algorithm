import sys
input = sys.stdin.readline
x = int(input())
# 0 ,1, 2, 3 의 최소 수 미리 저장
# 그 다음 수 부터 어떻게 했을때 최소 계산인지 계속해서 계산 (x가 구해질 때 까지)
li = [0,0,1,1]
for i in range(4, x+1):
    # 세가지 모두 비교할 것
    li.append(li[i-1]+1) # 1뺐을때 몇번 해서 1이 되었는지 +1 하는건 방금 계산한 거 때문
    if i % 2 ==0:
        li[i] = min(li[i],li[i//2]+1) # 1 뺀거랑 i//2가 1이되기 위해 몇번 계산되었는지 비교
    # 1뺀 거랑 2로 나눈것 중 더 적은 계산으로 이미 계산 되었음
    if i % 3 ==0:
        li[i] = min(li[i],li[i//3]+1)

print(li[x])