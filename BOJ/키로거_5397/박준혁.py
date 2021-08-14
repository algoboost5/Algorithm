# 입력
n = int(input())

#입력만큼 반복
for _ in range(n):
    
    sentence = input()
    
    # 스택 두개 생성
    stack_1 = []
    stack_2 = []
    
    # '-' 일때 stack_1 pop
    for j in sentence:
        if j == '-':
            if stack_1:
                stack_1.pop()
        
        #   '>' 일때 stack_2 pop 해서 stack_1에 추가
        elif j == ">":
            if stack_2:
                stack_1.append(stack_2.pop())
                
                
        # '<' 일때 stack_1 pop해서 stack_2에 추가        
        elif j == "<":
            if stack_1:
                stack_2.append(stack_1.pop())
        
        # 이외의것 stack_1에 추가
        else:
            stack_1.append(j)
    
    
    # stack 2 뒤집기        
    stack_2.reverse()
    
    # 병합후 문자열로 출력~
    print("".join(stack_1+stack_2))