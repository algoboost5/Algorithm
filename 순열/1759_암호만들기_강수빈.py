import sys
from itertools import *

if __name__=="__main__":
    L, C = map(int, sys.stdin.readline().split())

    consonants = []
    vowels = []
    vowel_ = ['a', 'e', 'i', 'o', 'u']
    for letter in sys.stdin.readline().split():
        if letter in vowel_:
            vowels.append(letter)
        else:
            consonants.append(letter)

    total_ls = []
    for v_num in range(1, min(L-1, len(vowels)+1)):
        c_num = L-v_num

        v_com = combinations(vowels, v_num)
        c_com = combinations(consonants, c_num)

        for i in product(v_com, c_com):
            ls = sorted(list(i[0] + i[1]))
            total_ls.append(ls)

    total_ls.sort()
    for ls in total_ls:

        print(''.join(ls))


