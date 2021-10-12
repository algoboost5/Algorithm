import heapq

V, E= map(int, input().split())
start= int(input())

INF= int(1e9)
graph= [[] for _ in range(V+1)]
distance= [INF]* (V+1)
visited= [0]* (V+1)

# u에서 v로 가는 비용이 w
for _ in range(E):
    u, v, w= map(int, input().split())
    graph[u].append([v, w])

def dijkstra(start):
    q= []
    heapq.heappush(q, [0, start])
    distance[start]= 0

    while q:
        dist, now= heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            value= distance[now]+ i[1]

            if value < distance[i[0]]:
                distance[i[0]]= value
                heapq.heappush(q, [value, i[0]])

dijkstra(start)

for i in range(1, V+1):
    if distance[i]== INF:
        print("INF")
    else:
        print(distance[i])
