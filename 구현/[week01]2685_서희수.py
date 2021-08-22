
n = int(input())
result = []
for _ in range(n):
    n, a, b = (int(i) for i in input().split())
    t_a = ''
    t_b = ''
    x=10
    while a>0:
        a, mod = divmod(a,n)
        t_a +=str(mod)

    while b>0:
        b, mod = divmod(b,n)
        t_b +=str(mod)
        
    if len(t_a)>=len(t_b):
        t_b+=(len(t_a)-len(t_b))*'0'
    else:
        t_a+=(len(t_b)-len(t_a))*'0'
     
    NimSum = ''
    for i in range(len(t_b)):
        _, mod = divmod(int(t_a[i])+int(t_b[i]),n)
        NimSum+=str(mod)
     
    result.append((NimSum[::-1],n))

for i,n in result:
    print(int(i,n))
