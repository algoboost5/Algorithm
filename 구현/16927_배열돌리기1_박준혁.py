# temp 변수 생성, 초기 값 삽입, 배열돌리고, 비어있는 곳 -> temp 변수 안에 저장해두었던 값 넣어주기

import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2):
    	# x, y 는 돌려지는 배열중 가장 첫번째 배열 인덱스
        x, y = i, i
        temp = data[x][y]# 안쪽까지 고려해야함

        for j in range(i + 1, n - i):  # 왼쪽
            x = j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

        for j in range(i + 1, m - i):  # 아래쪽
            y = j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

        for j in range(i + 1, n - i):  # 오른쪽
            x = n - j - 1
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

        for j in range(i + 1, m - i):  # 위쪽
            y = m - j -1
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value

for i in range(n):
    for j in range(m):
        print(data[i][j], end=' ')
    print()