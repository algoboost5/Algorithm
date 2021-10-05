class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children_num = 0


def dfs(visited, nodes, edges, cur):
    visited.append(cur)

    for child in edges[cur]:
        if (child in visited):
            continue
        nodes[child].parent = nodes[cur]
        nodes, nodes[child].children_num = dfs(visited, nodes, edges, child)
        nodes[cur].children_num += nodes[child].children_num + 1

    return nodes, nodes[cur].children_num


def solution(n, wires):
    # initialize
    nodes = [Node(i) for i in range(n + 1)]
    root_idx = 0
    edges = [[] for i in range(n + 1)]
    for wire in wires:
        edges[wire[0]].append(wire[1])
        edges[wire[1]].append(wire[0])

    # root 구하기
    root_idx = 0
    max_num = 0
    for idx, edge_ls in enumerate(edges):
        if (max_num < len(edge_ls)):
            max_num = len(edge_ls)
            root_idx = idx

    # parent/children 구조 확인
    nodes, child_num = dfs([], nodes, edges, root_idx)

    # 최소 송전탑 개수 차이 구하기
    min_gap = float('inf')
    for node in nodes:
        cut_num = node.children_num + 1
        gap = abs((n - cut_num) - cut_num)

        min_gap = min(min_gap, gap)

    return min_gap