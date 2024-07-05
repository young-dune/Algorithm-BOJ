import sys

input = sys.stdin.readline
n = int(input())

for i in range(1,n+1):
    num = sum((map(int,str(i))))
    result = num + i
    if result == n:
        print(i)
        break
    elif i == n:
        print(0)