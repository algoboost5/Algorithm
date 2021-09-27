
n, k= map(int, input().split())
# 각 물건별로 무게당 가질 수 있는 최고의 가치 배열을 설정 -> 2차원 리스트
dp= [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    weight, value= map(int, input().split())

    for j in range(1, k+1):
        # weight보다 작은 값인 경우에는 이전 값 가져오기
        if j < weight:
            dp[i][j]= dp[i-1][j]
        # weight보다 클 경우부터 이제 weight를 추가한 경우와 아닌 경우를 비교
        dp[i][j]= max(dp[i-1][j-weight]+ value, dp[i-1][j])
    # for l in dp:
    #     print(l)
    # print()

print(dp[n][-1])