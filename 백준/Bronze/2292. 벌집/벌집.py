n = int(input())
nBox = 1
cnt = 1

while n > nBox:
    nBox += 6*cnt
    cnt += 1
print(cnt)