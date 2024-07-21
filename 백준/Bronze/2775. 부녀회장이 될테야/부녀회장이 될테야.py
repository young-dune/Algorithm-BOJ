t = int(input())

    #3층 1 5 15 35 ...
    #2층 1 4 10 20 ...
    #1층 1 3 6 10 ...
    #0층 1 2 3 4 ...

for _ in range(t):
    k = int(input()) #k층
    n = int(input()) #n호
    people = [i for i in range(1,n+1)] #0층 i호에 i명
    
    for x in range(k): #k층은 0층부터 
        for y in range(1,n): #n호는 1호부터
            people[y] += people[y-1]
    print(people[-1])