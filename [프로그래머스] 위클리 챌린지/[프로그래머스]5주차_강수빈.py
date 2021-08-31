from itertools import product
def solution(word):
    
    word_dict = []
    for len in range(1,6):
        word_dict.extend(list(map(''.join, product('AEIOU', repeat=len))))
    word_dict.sort()
    
    return word_dict.index(word)+1
