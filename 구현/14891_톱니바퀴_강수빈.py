import sys

# 각 바퀴별로 움직일지 말지 결정
def get_cur_adj(wheel_ls):
    adj_ls = [0]
    for w_idx in range(1, 4):
        if(wheel_ls[w_idx][2] == wheel_ls[w_idx+1][6]) : adj_ls.append(True)
        else: adj_ls.append(False)

    return adj_ls

# 방향에 따라 바퀴 하나 rotate
def rotate_wheel(wheel, r_direc):
    if(r_direc==-1):
        # print("rotate left", wheel)
        tmp = wheel[0]
        del wheel[0]
        wheel.append(tmp)

    else:
        # print("rotate right", wheel)
        tmp = wheel[-1]
        del wheel[-1]
        wheel.insert(0, tmp)

    return wheel

# 방향에 따라 한쪽만 rotate 전파
def rotate_oneway(start_wheel, r_direc, m_direc, wheel_ls, cur_adj):
    # print("rotate_oneway", start_wheel, m_direc)
    if(start_wheel>1 and m_direc==-1):
        if not cur_adj[start_wheel-1]:
            wheel_ls[start_wheel-1] = rotate_wheel(wheel_ls[start_wheel-1], -1*r_direc)
            wheel_ls = rotate_oneway(start_wheel-1, -1 * r_direc, m_direc, wheel_ls, cur_adj)

    if(start_wheel<4 and m_direc==1):
        if not cur_adj[start_wheel]:
            wheel_ls[start_wheel+1] = rotate_wheel(wheel_ls[start_wheel+1], -1 * r_direc)
            wheel_ls = rotate_oneway(start_wheel+1, -1 * r_direc, m_direc, wheel_ls, cur_adj)


    return wheel_ls

# move left : -1, move right: 1
# 양쪽 모두 rotate
def rotate_twoway(start_wheel, r_direc, wheel_ls, cur_adj):
    # print("rotate_twoway", start_wheel)

    if(start_wheel>1):
        if not cur_adj[start_wheel-1] :
            wheel_ls[start_wheel-1] = rotate_wheel(wheel_ls[start_wheel-1], -1*r_direc)
            wheel_ls = rotate_oneway(start_wheel-1, -1*r_direc , -1,  wheel_ls, cur_adj)

    if(start_wheel<4):
        if not cur_adj[start_wheel]:
            wheel_ls[start_wheel + 1] = rotate_wheel(wheel_ls[start_wheel + 1], -1 * r_direc)
            wheel_ls = rotate_oneway(start_wheel+1, -1*r_direc, 1, wheel_ls, cur_adj)

    wheel_ls[start_wheel] = rotate_wheel(wheel_ls[start_wheel], r_direc)
    return wheel_ls





wheel_ls=[[0]*8]

for _ in range(4):
    wheel_ls.append(list(map(int, list(sys.stdin.readline().strip()))))

rotate_n = int(sys.stdin.readline())

for _ in range(rotate_n):
    start_wheel, direc = map(int,sys.stdin.readline().split())
    wheel_ls = rotate_twoway(start_wheel, direc, wheel_ls, get_cur_adj(wheel_ls))


result = 0
for w_idx in range(1,5):
    result += 2**(w_idx-1)*wheel_ls[w_idx][0]

print(result)

