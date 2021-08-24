import sys
sys.setrecursionlimit(10000000)
# input = sys.stdin.readline
# test case 수 
input_n= int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    global cnt
    land[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1<nx<r and -1<ny<c and land[nx][ny]==1:
            dfs(nx,ny)
            
result = []
for _ in range(input_n):
# 배추 더미를 담을 곳
    cnt=0
    # c:가로길이, r: 세로길이, n: 배추 위치 수
    # 땅 리스트 만들어줌     
    c, r, n = map(int,input().split())
    land = []
    for _ in range(r):
        land.append([0]*c)

    # 땅에 배추 위치에 1로 값 입력
    for _ in range(n):
        j, i = map(int,input().split())
        land[i][j]=1
    # 땅을 돌아다니며 배추무리 개수 세기
#     cnt는 한 더미에 있는 배추 수
    for i in range(r):
        for j in range(c):
            if land[i][j] == 1:
                dfs(i,j)
                cnt+=1
    result.append(cnt)

for repeat in range(input_n):
    print(result[repeat])
