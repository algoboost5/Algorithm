def solution(n, left, right):
    start_x= left//n
    end_x= right//n
    
    res= []
    for idx in range(start_x, end_x+1):
        ans= [idx+1] * (idx+1) + [i for i in range(idx+2, n+1)]
        
        res+= ans
        # print(res)
    return res[left- start_x*n : right+1- start_x*n]
