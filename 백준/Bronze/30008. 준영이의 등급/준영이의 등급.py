n,k = map(int, input().split())
g = list(map(int, input().split()))
result = []

for i in g:
    
    i = i * 100 // n
    
    if 0 <= i <= 4:
        result.append(1)
    elif 4 < i <= 11:
        result.append(2)
    elif 11 < i <= 23:
        result.append(3)
    elif 23 < i <= 40:
        result.append(4)
    elif 40 < i <= 60:
        result.append(5)
    elif 60 < i <= 77:
        result.append(6)
    elif 77 < i <= 89:
        result.append(7)
    elif 89 < i <= 96:
        result.append(8)
    elif 96 < i <= 100:
        result.append(9)
    
for i in result:
    print(i, end = " ")