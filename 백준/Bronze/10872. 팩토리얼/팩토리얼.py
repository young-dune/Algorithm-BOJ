
def fact(n):
    sum = 1
    if n > 1:
        sum = n* fact(n-1)
    return sum

n = int(input())
print(fact(n))