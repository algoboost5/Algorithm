
n= int(input())
dp= [0]* (n+1) # n=1인 경우도 고려하기 위해 dp[0]을 만들어 줌!

num= [i for i in range( n+1)]
for i in range(2, n+1):

    dp[i]= dp[i-1] +1 # 일단 default로 -1한거랑 비교를 하는 느낌
    if i%3==0: dp[i]= min(dp[i//3] +1, dp[i]) # 둘 다 if로 구현을 해주게 되면 둘 다 나눠질 경우도 고려
    if i%2==0: dp[i]= min(dp[i//2]+1, dp[i])

print(dp[n])