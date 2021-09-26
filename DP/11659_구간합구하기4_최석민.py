
# 주어진 입력 중 가장 멀리 있는 값을 찾아서 거기까지만 dp를 만들고,
# 값을 구해주는 느낌.. dp[y]- dp[x-1] 차이로

n, m= map(int ,input().split())
num= list(map(int, input().split()))
dp= [0]*(n+1)
max_y= 0

ans= []
for i in range(m):
    x, y= map(int, input().split())
    max_y= max(y, max_y)
    ans.append([x, y])

for i in range(1, max_y+1):
    dp[i]= dp[i-1]+ num[i-1]

for x, y in ans:
    print(dp[y]-dp[x-1])