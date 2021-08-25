def solution(table, languages, preference):
    table_2={i.split()[0]:i.split()[1:] for i in  table}
    
    result = []
    key = list(table_2.keys())
    key.sort()
    for i in key:
        sum_score=0
        for n,j in enumerate(languages):
            if j in table_2[i]:
                score = preference[n]
                score*=(5-table_2[i].index(j))
                sum_score+=score
        result.append(sum_score)
    
    return key[result.index(max(result))]
