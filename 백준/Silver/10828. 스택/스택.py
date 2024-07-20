import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    line = list(input().split())
    if line[0] == 'push':
        stack.append(line[1])
    elif line[0] == 'pop':
        if len(stack) > 0:
            x = stack.pop()
            print(x)
        else:
            print(-1)
    elif line[0] == 'size':
        print(len(stack))
    elif line[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif line[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])