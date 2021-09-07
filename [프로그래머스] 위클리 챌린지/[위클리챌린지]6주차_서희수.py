def solution(weights, head2head):
    answer = []
    # [승률,무거운상대 승리 횟수,몸무게,선수번호]
    num = 1
    for i,j in zip(weights, head2head):
        li = [0,0,i,num]
        match_count = len(j.replace("N",""))
        if match_count != 0:
            for n,score in enumerate(j):
                if score=="W":
                    li[0] += 1
                    if weights[n]>i:
                        li[1]+=1

            li[0] = li[0]/match_count
        num+=1
        answer.append(li)
    answer = sorted(answer, key = lambda x : (-x[0], -x[1], -x[2], x[3]))
    print(answer)
    return [result[-1] for result in answer]