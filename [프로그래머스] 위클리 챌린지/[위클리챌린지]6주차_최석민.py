
def solution(weights, head2head):
    result= []
    profile= [[0, 0, 0, 0] for _ in range(len(weights))] # 승률, 무거운 승리 횟수, 몸무게, 선수 번호

    for idx, value in enumerate(weights):
        total_cnt= 0
        win_cnt, over_cnt= 0, 0
        for idx_2, res in enumerate(head2head[idx]):
            if res== 'N': continue
            if res== 'W':
                if weights[idx] < weights[idx_2]:
                    over_cnt+=1
                win_cnt+=1
            total_cnt+=1
        if total_cnt==0: # 경기가 한 번도 안치뤄진 경우 경우
            profile[idx][1], profile[idx][2], profile[idx][3] = over_cnt, weights[idx], idx
            continue

        profile[idx][0], profile[idx][1], profile[idx][2], profile[idx][3]= win_cnt/total_cnt, over_cnt, weights[idx], idx

    profile= sorted(profile, key= lambda x:x[3]) # idx 순으로 정렬
    profile= sorted(profile, key= lambda x: (x[0], x[1], x[2]), reverse= True) # reverse 방식으로 순차적으로 정렬

    for i in profile:
        result.append(i[-1]+1)
    return result


# solution([50,82,75,120],
#          ["NLWL","WNLL","LWNW","WWLN"])

solution([60,70,60],
         ["NNN","NNN","NNN"])