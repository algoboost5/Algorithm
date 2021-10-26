
from collections import deque

# deque의 rotate 함수를 이용하면 보다 간단하게 회전할 수 있다 !
tires= [deque(list(input())) for _ in range(4)]
k= int(input())
rotates= [list(map(int, input().split())) for _ in range(k)]

for idx, dir in rotates:
    idx-=1

    tmp_R= tires[idx][2]
    tmp_L= tires[idx][6]
    tires[idx].rotate(dir)

    # 왼쪽 dir
    tmp_dir= dir
    for i in range(idx-1, -1, -1):
        if tires[i][2] != tmp_L:
            tmp_L= tires[i][6]
            tires[i].rotate(-tmp_dir)
            tmp_dir = -tmp_dir
        else: break;

    # 오른쪽 dir   
    tmp_dir = dir
    for i in range(idx+1, 4):
        if tires[i][6] != tmp_R:
            tmp_R= tires[i][2]
            tires[i].rotate(-tmp_dir)
            tmp_dir= -tmp_dir
        else: break;

    # for i in tires:
    #     print(i)
    # print()

result= 0
for i, tire in enumerate(tires):
    result+= (2**i)* int(tire[0])
print(result)
