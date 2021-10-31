from itertools import permutations
def solution(k, dungeons): 
    answer = 0
    
    for n in permutations([i for i in range(len(dungeons))]):
        ktemp = k # 초기피로도
        temp = 0 # 저장소  
        
        for index in n:
            mink, consumption = dungeons[index] 
            if ktemp >= mink: # 초기값이 최소필요피로도 보다 작거나 같을 경우
                ktemp -= consumption # 피로도에서 소모시켜요
                temp += 1 # 저장소에 횟수추가
                
        answer = max(temp, answer) # 최대값으로 저장
    return answer