import sys




n, m = map(int, sys.stdin.readline().split())
node_edge = [[] for _ in range(n+1)]
for _ in range(m):
    node1, node2 = map(int, sys.stdin.readline().split())
    node_edge[node1].append(node2)
    node_edge[node2].append(node1)

visited = []
stack = []
cur = 0
connected = 0
for node in range(1, n+1):
    if node in visited:
        continue
    else:
        stack.append(node)
        connected+=1
        while stack:
            cur = stack[0]
            del stack[0]
            visited.append(cur)
            for node2 in node_edge[cur]:
                if node2 not in visited:
                    visited.append(node2)
                    stack.append(node2)


print(connected)
