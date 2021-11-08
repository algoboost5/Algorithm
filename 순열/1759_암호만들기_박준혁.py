from itertools import *

L,C = map(int,input().split())

vowel = ['a','e','i','o','u']
my_consonant = []
my_vowel = []
centence = []

for text in input().split():
    if text in vowel:
        my_vowel.append(text)
    else:
        my_consonant.append(text)

for i in range(1, L-1):
    v = list(combinations(my_vowel,i))
    c = list(combinations(my_consonant,L-i))

    for j in product(v,c):
        answer = sorted(list(j[0]+j[1]))
        centence.append(answer)

centence.sort()
for k in centence:
    print(''.join(k))