n = int(input())
ball = list(map(int,input().split()))
result = 0
ball.sort()

for i in range(n-1):
    length = abs(ball[i]-ball[i+1])
    result += length

result += abs(ball[-1]-ball[0])

print(result)