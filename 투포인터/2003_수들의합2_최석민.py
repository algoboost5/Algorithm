n, m= map(int, input().split())
arr= list(map(int, input().split()))

start, end= 0, 1
cnt= 0
# print(arr)
while start <= end and end< len(arr):

    # 일치한다면 end 이동
    if sum(arr[start: end])== m:
        # print(start, end)
        cnt+=1
        end+=1
    
    # 합이 더 작다면 합을 키워주기 위해 End+
    elif sum(arr[start: end]) < m:
        end+=1
    # 합이 더 크다면 합을 작게 해주기 위해 start+
    elif sum(arr[start: end])> m:
        start+=1
print(cnt)
