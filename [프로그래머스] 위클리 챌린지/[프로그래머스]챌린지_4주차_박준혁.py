def solution(table, languages, preference):  # 모두 list 로 입력됨 , table은 모든 테스트케이스에서 동일합니다.
    # table_list = []
    for x in range(len(table)):
        table[x] = table[x].split()
    
    
    answer = ''
    max_num = 0
    leader = []
    
    for i in range(5): #table 의 길이 5 고정
        score = 0
        for j in range(len(languages)):
            if languages[j] in table[i]:
                score += preference[j] * (6-table[i].index(languages[j]))


        if score > max_num:
            max_num = score
            leader = [table[i][0]]
            
        elif score == max_num:
            max_num = score
            leader.append(table[i][0])
            
    return sorted(leader)[0]
