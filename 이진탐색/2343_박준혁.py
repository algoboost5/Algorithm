n, m = map(int, input().split())
num_list = list(map(int, input().split()))

left, right = max(num_list), sum(num_list)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    temp = 0

    for i in range(n):
        if temp + num_list[i] > mid:
            cnt += 1
            temp = 0

        temp += num_list[i]

    cnt += 1 if temp else 0

    if cnt <= m:
        right = mid - 1
        
    else:
        left = mid + 1

print(left)
# left와 right를 설정해주고 반복문을 통해 얻어진 리스트의 합이 mid보다 커지면 cnt(블루레이 개수)를 1씩 증가시킨다.
#  이렇게 얻은 블루레이 개수가 m보다 작으면 right를 줄여주고, m보다 크다면 left를 늘려준다. 