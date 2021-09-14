import sys

def check_ok(liqs, goal):

    left = 0
    right = len(liqs)-1
    # print(liqs, goal)
    while True:
        sum = abs(liqs[left] + liqs[right])
        # print(left, right, sum)
        if(sum <= goal):
            return [liqs[left], liqs[right]]
        else:
            if abs(liqs[left]) < abs(liqs[right]):
                right -= 1
            else:
                left += 1
            if(right <= left):
                return []

import sys

n = int(sys.stdin.readline())
liqs = sorted(list(map(int, sys.stdin.readline().split())))
liqs_abs = sorted(list(map(abs, liqs)))

if(liqs[0]>0):
    print(liqs[0], liqs[1])
elif (liqs[-1]<0):
    print(liqs[-2], liqs[-1])
else:

    # 첫번째 방법 - 이진 탐색
    max_val = liqs_abs[-1] + liqs_abs[-2]
    min_val = 0

    while min_val<=max_val:
        mid_val = (min_val+max_val)//2
        # print("min", "max", "mid", min_val,max_val,mid_val)
        result = check_ok(liqs, mid_val)
        if result :
            max_val = mid_val - 1
        else:
            min_val = mid_val + 1

    result = check_ok(liqs, min_val)
    print(result[0], result[1])


    # 두번째 방법 - 이진 탐색 x
    # left = 0
    # right = len(liqs) - 1
    # 
    # min_val = float('inf')
    # pair = ''
    # while True:
    # 
    #     sum = abs(liqs[left] + liqs[right])
    #     if (sum < min_val) :
    #         min_val = sum
    #         pair = str(liqs[left]) + ' ' + str(liqs[right])
    #     if abs(liqs[left]) < abs(liqs[right]):
    #         right -= 1
    #     else:
    #         left += 1
    # 
    #     if left == right:
    #         break
    # 
    # print(pair)
