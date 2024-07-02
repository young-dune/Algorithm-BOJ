matrix = [[0]*100 for _ in range(100)]
cnt = 0
n = int(input())

for _ in range(n):
    x,y = map(int, input().split())
    for a in range(x,x+10):
        for b in range(y,y+10):
            if matrix[a][b] == 0:
                matrix[a][b] = 1
                cnt+=1
print(cnt)