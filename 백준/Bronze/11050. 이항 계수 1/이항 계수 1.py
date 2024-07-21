n,k = map(int,input().split())

def fact(x):
    sum = 1
    for i in range(2,x+1):
        sum *= i
    return sum

result = fact(n) / (fact(n-k)*fact(k))
print(int(result))