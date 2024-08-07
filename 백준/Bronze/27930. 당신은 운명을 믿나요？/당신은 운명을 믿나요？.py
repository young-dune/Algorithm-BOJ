S = input() #점괘 S

#무조건 점괘안에 KOREA 또는 YONSEI가 존재해야 함.
#모두 찾을 경우, 먼저 찾은 학교에 합격.
#5 <= S <= 500,000
a = 0
b = 0

korea = 'KOREA'
yonsei = 'YONSEI'

for i in S:
    if a < 5 and i == korea[a]:
        a += 1
    if b < 6 and i == yonsei[b]:
        b += 1
    if a == 5:
        print('KOREA')
        break
    elif b == 6:
        print('YONSEI')
        break