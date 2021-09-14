n = int(input())

num_list = list(map(int,input().split()))

num_list.sort()

left = 0

right = n-1

answer = num_list[left] + num_list[right]

answer_left = left
answer_right = right

while left < right :
    tmp = num_list[left] + num_list[right]
    
    if abs(tmp) < abs(answer):
        answer = tmp
        answer_left = left
        answer_right = right
        
        if answer == 0:
            break
            
    if tmp < 0:
        left += 1
        
    else:
        right -= 1
        
print(num_list[answer_left],num_list[answer_right])