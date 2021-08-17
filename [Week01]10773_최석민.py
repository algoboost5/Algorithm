
k= int(input())
stack= []
for i in range(k):
    value= int(input())
    if value==0:
        stack.pop(); continue;
    stack.append(value)
print(sum(stack))