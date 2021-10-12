from itertools import combinations


# 근 구하기
def get_solution(line1, line2):
    a1, b1, c1 = line1
    a2, b2, c2 = line2
    if (a1 * b2 == a2 * b1):
        return None

    x = - (b1 * c2 - b2 * c1) / (a2 * b1 - a1 * b2)
    y = - (- a1 * c2 + a2 * c1) / (a2 * b1 - a1 * b2)

    if x == int(x) and y == int(y):
        return (int(x), int(y))
    else:
        return None


def solution(line):
    int_point = []
    combi = combinations(line, 2)
    x = []
    y = []
    for line1, line2 in combi:
        answer = get_solution(line1, line2)
        if (answer):
            int_point.append(answer)
            x.append(answer[0])
            y.append(answer[1])

    # map initialize
    min_x, max_x, min_y, max_y = min(x), max(x), min(y), max(y)
    width = (max_x + 1 - min_x)
    height = (max_y + 1 - min_y)
    answer = [['.'] * (max_x + 1 - min_x) for _ in range(min_y, max_y + 1)]

    # map에서 *로 바꾸기
    for point in int_point:
        w = point[0] - min_x
        h = height - (point[1] - min_y) - 1
        answer[h][w] = '*'

    for idx, line in enumerate(answer):
        answer[idx] = ''.join(line)

    return answer