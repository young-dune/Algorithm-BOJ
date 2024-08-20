'''
    최대 이익을 위해서 최대한 최저가에 사서 최고가에 판매한다.
'''
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.reverse()
    #뒤에서부터 주가를 탐색한다.
    
    res = 0
    maxPrice = 0

    for i in range(n):
        if maxPrice < arr[i]:
            maxPrice = arr[i]
        res += maxPrice - arr[i]

    print(res)