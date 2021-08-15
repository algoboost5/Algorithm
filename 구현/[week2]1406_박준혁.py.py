from sys import stdin

stack_sentence = list(stdin.readline().strip())
stack_1 = []
n = int(input())

for _ in range(n):
    temp = stdin.readline()
    
    if temp[0] == 'L':
        if len(stack_sentence) == 0:
            continue
        stack_1.append(stack_sentence.pop())

    elif temp[0] == 'D':
        if len(stack_1) == 0:
            continue
        stack_sentence.append(stack_1.pop())

    elif temp[0] == 'B':
        if len(stack_sentence) == 0:
            continue
        stack_sentence.pop()

    elif temp[0] == 'P':
        stack_sentence.append(temp[2])

stack_1.reverse()

stack_sentence.extend(stack_1) 

print("".join(stack_sentence))