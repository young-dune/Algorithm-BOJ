n = int(input())
sum = 0

for _ in range(n):
    a,b,c = map(int,input().split())
    if a == b == c:
        sum = max(sum, 10000+ a*1000)
    elif a == b:
        sum = max(sum, a*100 + 1000)
    elif b == c:
        sum = max(sum, b*100 + 1000)
    elif a == c:
        sum = max(sum, c*100 + 1000)
    else:
        sum = max(sum, max(a,b,c)*100)

print(sum)