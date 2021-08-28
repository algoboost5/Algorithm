import sys
# input = sys.stdin.readline

n= int(input())
color = input()
red_paint = 1
blue_paint = 1

# blue
for i in range(n):
    if color[i]!='B':
        red_paint+=1
        if n-i>1:
            if color[i+1]!='B':
                red_paint-=1
    
#red
for i in range(n):
    if color[i]!='R':
        blue_paint+=1
        if n-i>1:
            if color[i+1]!='R':
                blue_paint-=1

print(min(blue_paint,red_paint))
