import sys

prob_num = int(sys.stdin.readline())
problems = sys.stdin.readline().strip()
probs = [problems[0]]
#BBRRBBRRR-> BRBR
for p in problems:
    if probs[-1] != p:
        probs.append(p)


# #1) BRBRBR case
# if probs[0] == probs[-1]:
#     print(len(probs)//2+1)
# #2) BRBRBRB case
# else:
#     print(len(probs)//2+1)

print(len(probs) // 2 + 1)
