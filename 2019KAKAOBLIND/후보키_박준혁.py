# 유일성 -> 최소성
from itertools import combinations

candidate = []

# 유일성
def unique(r,c):
    student = []
    
    for i in r:
        data = []
        for j in c:
            data.append(i[j])
        student.append(tuple(data))
        
    if len(set(student)) == len(r):
        return 1
    else:
        return 0
    
# 최소성
def mini(c):
    for i in candidate:
        if i.issubset(c): # issubset 부분집합
            return 0
    return 1

def solution(relation):
    answer = 0
    n = len(relation[0])
    attri = [i for i in range(n)]
    
    combination = []
    for i in range(1,n+1):
        combination.extend(map(set,combinations(attri, i)))
        
    for i in combination:
        if mini(i):
            if unique(relation,i):
                answer += 1
                candidate.append(i)
                
    return answer