import sys
# input = sys.stdin.readline
n,m = map(int,input().split())
row=[]
col=[]
result = 0
for _ in range(m):
    r,c = map(int,input().split())
    row.append(r)
    col.append(c)
mid = m//2
row_mid = sorted(row)[mid]
col_mid = sorted(col)[mid]
for i,j in zip(row,col):
    result+=abs(i-row_mid)
    result+=abs(j-col_mid)
print(result)
