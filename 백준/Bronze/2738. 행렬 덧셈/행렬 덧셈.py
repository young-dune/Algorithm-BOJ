n,m = map(int, input().split())
a,b = [],[]

for i in range(n):
    x = list(map(int,input().split()))
    a.append(x)

for j in range(n):
    y = list(map(int, input().split()))
    b.append(y)
    
for i in range(n):
    for j in range(m):
        sum = a[i][j]+b[i][j]
        print(sum, end=' ')
    print()