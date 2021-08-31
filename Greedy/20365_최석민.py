
n= int(input())
color_list= list(input())
cnt= 0
set_color= [color_list[0]]
for idx in range(1, len(color_list)):
    if set_color[-1]!=color_list[idx]:
        set_color.append(color_list[idx])

B_count, R_count= 1, 1
for color in set_color:
    if color=='R': B_count+=1
    else: R_count+=1

print(min(B_count, R_count))