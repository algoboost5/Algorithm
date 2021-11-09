def solution(n, left, right):
    answer = []
    for i in range(left,right+1): # n*n으로 구현시 시간초과
        answer.append(max(i//n,i%n)+1) # n으로 나눈 몫과 나머지에서 큰값에 +1
    return answer