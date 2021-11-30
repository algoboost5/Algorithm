from itertools import combinations


def chk_possible(relations, candidate_keys):
    tuples = []
    for relation in relations:
        stu_info = []
        for c_key in candidate_keys:
            stu_info.append(relation[c_key])
        if (stu_info in tuples):
            return False
        tuples.append(stu_info)

    return True


def search_keys(relations, left_keys, key_num, max_depth, found_keys):
    total = 0
    key_list = []

    # step1 : 현재 level에서 선택할 key의 개수에 따라 key들의 combination을 구한다.
    key_combi = combinations(left_keys, key_num)
    key_combi = list(key_combi)

    # step2 : key combination중 후보 키가 될 수 있는 key들을 판단한다.
    for keys in key_combi:
        keys = set(keys)
        if (chk_possible(relations, keys)):
            minimum = True
            for cur_key in found_keys:
                if (cur_key.issubset(keys)):
                    minimum = False
                    break
            if (minimum):
                total += 1
                key_list.append(keys)

    # step3 : 선택하는 key의 개수를 하나씩 늘려서 가능한 모든 후보키를 찾는다.
    if key_num < max_depth:
        val, key_li = search_keys(relations, left_keys, key_num + 1, max_depth, found_keys + key_list)
        total += val
        key_list.extend(key_li)

    return total, key_list


def solution(relations):
    max_depth = len(relations[0])
    answer, key_list = search_keys(relations, [i for i in range(max_depth)], 1, max_depth, [])

    return answer