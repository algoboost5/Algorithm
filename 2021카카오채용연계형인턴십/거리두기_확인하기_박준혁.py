# BFS 로 해결.?
from collections import deque 

moving_x = [1,0,-1,0]
moving_y = [0,-1,0,1]

def bfs(place, i, j):
    visit = [[0] * 5 for _ in range(5)]
    q = deque()
    q.append((i,j,0))
    visit[i][j] = 1
    
    while q:
        x,y, dist = q.popleft()
        if 0 < dist < 3 and place[x][y] =='P': # 거리 2 이내만 확인하고 P 유무 확인
            return False

        if dist > 2:
            break
            
        for k in range(4):
            nx, ny, nd = x + moving_x[k], y + moving_y[k], dist+1
            if 0 <= nx < 5 and 0 <= ny < 5:
                if place[nx][ny] != 'X' and not visit[nx][ny]:
                    q.append((nx,ny,nd))
                    visit[nx][ny] =1
    return True
            
        
        
def solution(places):
    answer = []
    
    for place in places:
        checkpoint = 0
        
        for i in range(len(place)):
            for j in range(len(place[0])):
                if place[i][j] == "P":
                    if not bfs(place, i, j):
                        answer.append(0)
                        checkpoint = 1
                        break
            if checkpoint:
                break
        else:
            answer.append(1)

    return answer