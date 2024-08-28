import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    ques = input().split()
    
    if ques[0] == '1':
        stack.append(ques[1])
    elif ques[0] == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif ques[0] == '3':
        print(len(stack))
    elif ques[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif ques[0] == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])