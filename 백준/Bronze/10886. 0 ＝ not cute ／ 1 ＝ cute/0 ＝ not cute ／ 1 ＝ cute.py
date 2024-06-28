n = int(input())
cnt1 = 0
cnt2 = 0

for _ in range(n):
    answer = int(input())
    
    if answer == 1:
        cnt1 += 1
    elif answer == 0:
        cnt2 += 1

if cnt1 > cnt2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")