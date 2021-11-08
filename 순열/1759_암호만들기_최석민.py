from itertools import combinations # 알파벳 숫자가 크지 않으니까..!

mo= ['a', 'i', 'o', 'u', 'e']

L, C= map(int, input().split())
word= list(input().split())
mo_word= []
ja_word= []

for w in word:
    if w in mo:
        mo_word.append(w)
        continue
    ja_word.append(w)

result= []
for i in range(1, L-1):
    m= list(combinations(mo_word, i))
    j= list(combinations(ja_word, L-i))

    for k in m:
        for l in j:
            if ''.join(sorted(k + l)) not in result:
                result.append(''.join(sorted(k + l)))

for res in sorted(result):
    print(res)
