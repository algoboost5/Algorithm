import sys
from collections import deque

input = sys.stdin.readline()
p_list = list(input)[0:-1]

stack = deque()

def parenthesis(stack):
    for i in range(len(p_list)):
        stack.append(p_list[i])

        if stack[-1] == ')':
            stack.pop()

            tmp_sum = 0
            try:
                while stack[-1] != '(':
                    tmp_sum = tmp_sum + stack.pop()
            except:
                return 0

            if tmp_sum == 0:
                stack[-1] = 2
            else:
                stack[-1] = tmp_sum * 2

        elif stack[-1] == ']':
            stack.pop()

            tmp_sum = 0
            try:
                while stack[-1] != '[':
                    tmp_sum = tmp_sum + stack.pop()
            except:
                return 0

            if tmp_sum == 0:
                stack[-1] = 3
            else:
                stack[-1] = tmp_sum * 3

    if '[' in stack or ']' in stack or '(' in stack or ')' in stack:
        return 0
    
    return sum(stack)


print(parenthesis(stack))