class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None


import sys
node_num = int(sys.stdin.readline())
nodes = ['',]
for idx in range(node_num):
    nodes.append(Node(idx+1))
nodes[1].height = 1

edges = [[] for _ in range(node_num+1)]
for _ in range(node_num-1):
    node1, node2 = map(int, sys.stdin.readline().split())
    edges[node1].append(node2)
    edges[node2].append(node1)

avail = [1]
while avail:
    cur = avail[0]
    for node in edges[cur]:
        if nodes[node].parent:
            continue
        else:
            avail.append(node)
            nodes[node].parent = cur
    del avail[0]

for idx in range(2, node_num+1):
    print(nodes[idx].parent)



