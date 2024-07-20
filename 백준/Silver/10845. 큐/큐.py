from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
Q = deque()

for _ in range(n):
    arr = list(input().split())
    if arr[0] == 'push':
        Q.append(arr[1])
    elif arr[0] == 'pop':
        if len(Q) > 0:
            x = Q.popleft()
            print(x)
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(Q))
    elif arr[0] == 'empty':
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    elif arr[0] == 'front':
        if len(Q) > 0:
            print(Q[0])
        else:
            print(-1)
    elif arr[0] == 'back':
        if len(Q) > 0:
            print(Q[-1])
        else:
            print(-1)