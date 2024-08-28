import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
Q = deque()

for _ in range(n):
    num = input().split()
    
    if num[0] == '1':
        Q.appendleft(num[1])
    elif num[0] == '2':
        Q.append(num[1])
    elif num[0] == '3':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.popleft())
    elif num[0] == '4':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.pop())
    elif num[0] == '5':
        print(len(Q))
    elif num[0] == '6':
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    elif num[0] == '7':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[0])
    elif num[0] == '8':
        if len(Q) == 0:
            print(-1)
        else:
            print(Q[-1])