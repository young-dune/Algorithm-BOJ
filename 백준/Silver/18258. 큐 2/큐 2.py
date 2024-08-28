import sys
from collections import deque
input = sys.stdin.readline
Q = deque()

n = int(input())

for _ in range(n):
    num = input().split()
    
    if num[0] == 'push':
        Q.append(num[1])
    elif num[0] == 'pop':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.popleft())
    elif num[0] == 'size':
        print(len(Q))
    elif num[0] == 'empty':
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    elif num[0] == 'front':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[0])
    elif num[0] == 'back':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[-1])