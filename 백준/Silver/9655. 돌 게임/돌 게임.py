n = int(input())
#게임은 sk가 먼저 시작한다.
'''
    n = 1, sk
    n = 2, cy
    n = 3, sk
    n = 4, cy
'''
if n % 2 == 0:
    print('CY')
else:
    print('SK')