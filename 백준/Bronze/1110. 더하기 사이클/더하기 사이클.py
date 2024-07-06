n = int(input())
cnt = 0
res = n

while(1):
    a1 = n // 10 #주어진 수의 10의 자리숫자=2
    a2 = n % 10 #주어진 수의 1의 자리숫자=6
    newNum =  a2*10 + (a2 + a1) % 10 
    cnt += 1
    n = newNum
    
    if n == res:
        break
print(cnt)