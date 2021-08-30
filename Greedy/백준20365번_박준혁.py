import sys
# BBRBRBBR
n = int(sys.stdin.leadline())
sentence = str(input())
count = {"B" : 0, "R" : 0}

count[sentence[0]] += 1

for i in range(n):
    if sentence[i] != sentence[i-1]:
        count[sentence[i]] += 1
        
print(min(count['B'], count['R'])+1)     