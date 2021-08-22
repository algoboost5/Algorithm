from collections import deque


def find_val(p_input):
    parens = {'(': 2, ')': 2, '[': 3, ']': 3}
    left_paren = ['(', '[']
    w_stack = deque([])

    if (p_input.count('(') != p_input.count(')') or p_input.count('[') != p_input.count(']')):
        return 0

    for p in p_input:
        if p in left_paren:
            w_stack.append(p)
        else:
            mul = 1
            mul_list = []
            while (True):
                left_p = w_stack.pop()
                if (type(left_p) == type(1)):
                    mul_list.append(left_p)
                else:
                    if (mul_list): mul = sum(mul_list)
                    break

            if (left_p not in left_paren or parens[left_p] != parens[p]):
                return 0
            else:
                w_stack.append(parens[left_p] * mul)
                # print(w_stack, p)

    return sum(w_stack)



p_input = input()
print(find_val(p_input))

