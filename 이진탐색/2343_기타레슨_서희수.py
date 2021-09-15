import sys
# input = sys.stdin.readline
input_n, num_vid = map(int,input().split())
li = list(map(int,input().split()))

# 크기를 정했을때 모든 영상이 들어가는지 체크
# mid는 하나의 강의에 들어갈 크기
def check(mid):
    n=0 # 몇개의 강의가 발생하는지 체크
    t=0 # mid보다 작을때 까지만 담는 곳
    for i in li:
        if t+i > mid:
            n+=1
            t=i
        else:
            t+=i
    return n+1<=num_vid


# 가장 큰 값 하나가 들어갔을때를 시작값으로, 각 강의의 길이는 10000분 넘기면 안 됨
start, end = max(li)-1, sum(li) # F~T를 다 포함하는 범위로 해야함 max(li)를 start로 두면 T로 시작하는 경우 발생
# start와 end의 사이 값이 있으면 계속 동작
while  start+1< end:
    mid = (end+start)//2
    if check(mid):
        end = mid # 강의의 크기가 작아 m개로 못만든다는 소리
    else:
        start = mid

# end이상의 값이 들어가야 True임, 최소값은 end
print(end) 
