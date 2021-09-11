import sys
# input = sys.stdin.readline
input_n = int(input())
li = sorted(list(map(int,input().split())))
# 시작값은 양 끝 값의 합의 절대값
answer = abs(li[0]+li[-1])
start = 0
end = input_n-1
# 합의 최소값일때의 위치
answer_start = start
answer_end = end

# start가 end보다 작을때 계속 돔 
while start<end:
    #  새로 더한 값
    plus = li[start]+li[end]
    # 비교해서 작으면 plus가 답으로 가고 최소값일때의 위치도 변경
    if abs(plus)<answer:
        answer = abs(plus)
        answer_start = start
        answer_end = end
    if answer==0:
        break
# 합이 0보다 크면 오른쪽값을 왼쪽으로 떙겨줌
# 합이 0보다 작으면 왼쪽값은 오른쪽으로 땡겨줌
    if plus>0:
        end-=1
    else:
        start+=1

print(li[answer_start],li[answer_end])
