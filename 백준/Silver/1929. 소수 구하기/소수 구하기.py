import math

m,n = map(int,input().split())
res = []
for i in range(m,n+1):
    if i == 1:
        continue
    for x in range(2,int(math.sqrt(i))+1):
        if i%x == 0:
            break
    else:
        print(i)