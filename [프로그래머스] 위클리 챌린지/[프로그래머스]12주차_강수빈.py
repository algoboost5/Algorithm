def solution(k, dungeons):
    dungeons.sort(reverse=True)
    for d in dungeons:
        if d[0] > k:
            del dungeons[0]
        else:
            break
    cnt = 0

    while (dungeons):
        max_survive = -1
        visit_dun = -1
        left_dun = []
        for d_idx, d in enumerate(dungeons):
            survive = 0
            left_dun_cur = []
            left_k = k - d[1]
            for idx in range(0, d_idx):
                if (left_k >= dungeons[idx][0]):
                    survive += 1
                    left_dun_cur.append(dungeons[idx])
            for idx in range(d_idx + 1, len(dungeons)):
                if (left_k >= dungeons[idx][0]):
                    survive += 1
                    left_dun_cur.append(dungeons[idx])

            if (max_survive < survive):
                max_survive = survive
                visit_dun = d_idx
                left_dun = left_dun_cur

        k -= dungeons[visit_dun][1]
        dungeons = left_dun

        cnt += 1

    return cnt