def sub(parents, money, number, answer):
    
    if parents[number] == number or money // 10 == 0: # 종료시스템
        answer[number] += money 
        return
    
    sending_money = money//10 # 상납금 전달
    my_money = money - sending_money # 내돈
    answer[number] += my_money 
    
    sub(parents, sending_money, parents[number], answer)
    return


def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = [0] * (n+1)
    
    dic = {} # name : number 딕셔너리 
    parents = [i for i in range(n+1)] 
    
    for i in range(n): # name : number dic에 저장
        dic[enroll[i]] = i + 1
    
    for i in range(n):
        # center가 추천인일 경우
        if referral[i] == "-": 
            parents[i+1] = 0
        # 그 외
        else:
            parents[i+1] = dic[referral[i]]


    for i in range(len(seller)):
        sub(parents, amount[i]*100, dic[seller[i]], answer)
    answer.pop(0) # center 제외
    return answer