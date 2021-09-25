# 1로 만들기

# 최적 부분 구조와 중복되는 부분 문제
n = int(input())

# DP Table 생성
D = [0] * (n+1) 

for i in range(2, n+1):
    # 현재의 수에서 1을 빼는 경우
    D[i] = D[i-1] + 1
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        D[i] = min(D[i], D[i//3] + 1)
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        D[i] = min(D[i], D[i//2] + 1)


print(D[n])