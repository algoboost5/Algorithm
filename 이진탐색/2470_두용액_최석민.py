
# 이진 탐색을 사용하려면 정렬이 되어 있어야 함 !
# 시작을 음의 가장 작은 수, 끝을 양의 가장 큰 수의 idx로 정의하고,
# 최대 n번 탐색을 하기

n= int(input())
liquid= sorted(list(map(int,input().split())))
start, end= 0, n-1
res= liquid[start]+ liquid[end]
res_idx= [0, n-1]
while start< end: # 서로 다른 두 용액 사용..
    val= liquid[start]+ liquid[end]

    if abs(val) < abs(res):
        res_idx[0], res_idx[1]= start, end
        res= val

    if val < 0:
        start+=1
    else: end-=1

# print(res)
print(liquid[res_idx[0]], liquid[res_idx[1]])

