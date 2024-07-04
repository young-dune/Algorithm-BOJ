while (1):
    a,b,c = map(int, input().split())
    if a==0 and b==0 and c==0:
        break
    #항상 c가 빗변이라는 보장이 없으니 가장 큰 숫자를 c로 보내서 직각삼각형을 판단한다.
    if max(a,b,c) == a:
        a,c = c,a
    elif max(a,b,c) == b:
        b,c = c,b
    
    
    if a**2 +  b**2 == c**2:
        print('right')
    else:
        print('wrong')
