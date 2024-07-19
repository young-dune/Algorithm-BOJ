n = int(input())
flag = 0

for i in range(n):
    str = input()
    if str == 'anj':
        flag = 1

if flag == 1:
    print("뭐야;")
else:
    print("뭐야?")