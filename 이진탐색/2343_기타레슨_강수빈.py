import sys

def check_ok(lectures, length, m) :
    sum = 0
    remain_m = m-1

    for lecture in lectures:
        if (lecture > length):
            return False

        sum += lecture
        if sum>length:
            remain_m-=1
            sum = lecture

    if(remain_m>=0):
        return True
    else:
        return False


n, m = map(int, sys.stdin.readline().split())
lectures = list(map(int, sys.stdin.readline().split()))

lectures_sort = sorted(lectures)
min_val = sum(lectures_sort[0:n//m])
max_val = sum(lectures_sort[-1*(n//m+1):])

while(min_val <= max_val) :
    mid_val = int((min_val+max_val)/2)
    if check_ok(lectures, mid_val, m):
        max_val = mid_val-1
    else:
        min_val = mid_val+1


print(min_val)