# 강의가 길이의 순서대로 자연수가 주어진다.
# 일단 길이의 순서대로 ? sort된 상태로 list가 주어진다는 것에서 이진탐색이라는 것을 살짝 의심을 해야함
# 결국 최소값을 찾는 문제... min 부터 전체 강의 sum까지 이진 탐색을 하는 것이 맞는 것 같음

n, m= map(int, input().split())
lecture= list(map(int, input().split()))

# 고치긴 했는데 왜.. 최소 값 사용하면 안되는지 ? 반례가 안떠오름..
start, end= max(lecture), sum(lecture)
res= 0

while start<= end:
    mid= (start+end)//2

    cnt, tmp_sum= 0, 0
    for i in range(n):
        if tmp_sum+ lecture[i] > mid:
            tmp_sum= lecture[i]; cnt+=1
        else: tmp_sum+= lecture[i]

    if cnt <= m-1:
        res= mid
        end= mid-1

    elif cnt> m-1:
        start= mid+1

print(res)





