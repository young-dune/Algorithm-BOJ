n,m = map(int,input().split())

box = [i for i in range(1,n+1)]

for _ in range(m):
    i,j = map(int,input().split())
    tmp = box[i-1]
    box[i-1] = box[j-1]
    box[j-1] = tmp

for x in box:
    print(x,end=' ')