import sys
input = sys.stdin.readline

house_num = int(input())

least_cost_mem = []
for i in range(house_num):
    least_cost_mem.append([0,0,0])


r,g,b = map(int, input().split())
least_cost_mem[0][0] = r
least_cost_mem[0][1] = g
least_cost_mem[0][2] = b
for i in range(1,house_num):
    r,g,b = map(int, input().split())

    least_cost_mem[i][0] = min(least_cost_mem[i-1][1],least_cost_mem[i-1][2])+r
    least_cost_mem[i][1] = min(least_cost_mem[i-1][0],least_cost_mem[i-1][2])+g
    least_cost_mem[i][2] = min(least_cost_mem[i-1][0],least_cost_mem[i-1][1])+b


print(min(least_cost_mem[house_num-1]))