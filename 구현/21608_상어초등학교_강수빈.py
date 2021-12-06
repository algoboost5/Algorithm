import sys

# 주변이 비었는지와 주변에 선호 학생이 있는지를 반환
def _cal(seat_map, coord, likes):
    vacant = 0
    adj = 0
    direcs = [(0,1), (1, 0), (0,-1), (-1, 0)]
    for direc in direcs:
        adj_x = coord[0]+direc[0]
        adj_y = coord[1]+direc[1]

        if(adj_x < 0 or adj_x>=len(seat_map) or adj_y<0 or adj_y>=len(seat_map)):
            continue
        if(seat_map[adj_x][adj_y]==0):
            vacant+=1
        elif(seat_map[adj_x][adj_y] in likes):
            adj+=1

    return vacant, adj

# 주변 친구들을 보고 학생의 만족도를 반환
def cal_adj_score(seat_map, coord, likes):
    adj = 0
    direcs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for direc in direcs:
        adj_x = coord[0] + direc[0]
        adj_y = coord[1] + direc[1]

        if (adj_x < 0 or adj_x >= len(seat_map) or adj_y < 0 or adj_y >= len(seat_map)):
            continue

        if (seat_map[adj_x][adj_y] in likes):
            adj += 1

    return 10**(adj-1) if adj>0 else 0


N = int(sys.stdin.readline())
seat_map = [[0]*N for _ in range(N)]
stu_likes = {}
for _ in range(N*N):
    line = list(map(int, sys.stdin.readline().split()))
    stu = line[0]
    likes = line[1:]
    stu_likes[stu] = likes
    candidate = []
    for i in range(N):
        for j in range(N):
            if seat_map[i][j] == 0:
                vacant, adj = _cal(seat_map, (i,j), likes)
                candidate.append([adj, vacant, i, j])
    # 조건에 맞게 sort
    candidate = sorted(candidate, key=lambda x: (-x[0], -x[1], x[2], x[3]))
    seat_map[candidate[0][2]][candidate[0][3]] = stu

score = 0
for i in range(N):
    for j in range(N):
        score += cal_adj_score(seat_map, (i, j), stu_likes[seat_map[i][j]])

print(score)




