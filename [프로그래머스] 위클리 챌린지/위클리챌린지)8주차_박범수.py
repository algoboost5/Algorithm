import sys

f = sys.stdin.readline


def solution(sizes):
    # max_x, max_y = 0, 0

    # for x, y in sizes:
    #     if (max_x < x or max_y < y) and (max_x < y or max_y < x):
    #         max_x = max(max_x, x)
    #         max_y = max(max_y, y)

    # print(max_x * max_y)

    # max_l = max([x[0] if x[0] > x[1] else x[1] for x in sizes])
    # print(max_l)

    # max_s = 0

    max_l, max_s = 0, 0

    for a, b in sizes:
        if a > b:
            l, s = a, b
        else:
            l, s = b, a

        max_l = max(max_l, l)
        max_s = max(max_s, s)

    print(max_l * max_s)
    return max_l * max_s


solution([[60, 50], [30, 70], [60, 30], [80, 40]])
solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])
