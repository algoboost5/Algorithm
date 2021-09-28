# 다시 풀어보기

sen1= input()
sen2= input()
dp= [[0]* (len(sen2)+1) for _ in range(len(sen1)+1)]

for i in range(1, len(sen1)):
    for j in range(1, len(sen2)):
        if sen1[i-1]== sen2[j-1]:
            dp[i][j]= dp[i-1][j-1]+ 1
        else:
            dp[i][j]= max(dp[i-1][j], dp[i][j-1])


print(dp[-1][-1])
