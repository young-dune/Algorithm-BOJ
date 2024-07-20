n,m = map(int,input().split())
arr = list(map(int,input().split()))
result = 0

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]+arr[k] > m:
                continue #3개 합이 m보다 클 경우 -> 배제
            else:
                result = max(result,arr[i]+arr[j]+arr[k]) #3개 합이 m보다 작을 경우 m에 가까울 수 있으니 계속해서 result값과 비교하여 max함수를 통해 더 큰 값으로 최신화


print(result)