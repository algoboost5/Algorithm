import sys

g_len, s_len = map(int, sys.stdin.readline().split())
W = sys.stdin.readline().strip()
S = sys.stdin.readline().strip()

w_set = set(W)
w_dict = {v:idx for idx, v in enumerate(w_set)}
w_cnt = [0]*len(w_set)
s_cnt = [w_cnt.copy()]
for w in W:
    w_cnt[w_dict[w]]+=1

for idx in range(0, g_len-1):
    append_cnt = s_cnt[-1].copy()
    # print(S[idx])
    if (S[idx] in w_set):
        append_cnt[w_dict[S[idx]]] += 1
    s_cnt.append(append_cnt)


answer = 0
for idx in range(g_len-1,s_len):
    append_cnt = s_cnt[-1].copy()
    if (S[idx] in w_set):
        append_cnt[w_dict[S[idx]]] += 1
    s_cnt.append(append_cnt)

    left = s_cnt[0]
    right = s_cnt[-1]
    correct = True
    for w_idx in range(len(w_set)):
        if right[w_idx]-left[w_idx]!=w_cnt[w_idx]:
            correct = False
            break
    if(correct) : answer+=1
    del s_cnt[0]

print(answer)
