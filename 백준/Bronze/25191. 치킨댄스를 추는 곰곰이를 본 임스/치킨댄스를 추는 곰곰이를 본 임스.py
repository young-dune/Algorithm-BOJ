n = int(input())
# n = Chicken
a,b = map(int,input().split())
# a = Coke, b = Beer

sum = int(a/2+ b)

if n > sum:
    print(sum)
elif n < sum:
    print(n)