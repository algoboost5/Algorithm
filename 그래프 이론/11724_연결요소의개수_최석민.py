
# 최상위 부모를 찾는 함수
def get_parent(parent, x):
    if parent[x]== x:
        return x
    return get_parent(parent, parent[x])

def union(parent, x, y):
    x= get_parent(parent, x)
    y= get_parent(parent, y)

    # 더 작은 노드를 부모로 !
    if x< y:
        parent[y]= x
    else:
        parent[x]= y

n, m= map(int, input().split())
parent= [0]* (n+1)
for i in range(1, n+1): # 부모 노드 초기화
    parent[i]= i

for _ in range(m):
    a, b= map(int, input().split())
    union(parent, a, b)

# print(parent)
result= []
for i in parent:
    result.append(get_parent(parent, i))

print(len(set(result[1:])))
