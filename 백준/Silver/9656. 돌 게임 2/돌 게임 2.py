n = int(input())
#게임은 sk가 먼저 시작한다.
'''
    n = 1, cy
    n = 2, sk
    n = 3, cy
    n = 4, sk
'''
if n % 2 == 0:
    print('SK')
else:
    print('CY')