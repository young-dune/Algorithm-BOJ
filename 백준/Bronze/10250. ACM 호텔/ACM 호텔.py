t=int(input())

for _ in range(t):
    h,w,n=map(int,input().split())
    num = (n//h)+1
    line = (n%h)
    
    # 6 12 6이라면, 102호가 돼야함.
    if line == 0:
        line = h
        num = num-1
    print(line*100 + num)