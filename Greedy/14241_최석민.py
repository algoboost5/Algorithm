n= int(input())
arr= list(map(int, input().split()))
score= 0

while len(arr)>1:
    arr= sorted(arr)
    max_value, min_value= arr.pop(), arr.pop(0)
    score+= max_value * min_value
    arr.append(max_value+ min_value)

print(score)