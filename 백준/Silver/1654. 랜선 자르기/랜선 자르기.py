import sys
input = sys.stdin.readline

k,n = map(int,input().split()) #k:이미 있는 랜선, n:필요한 랜선
arr = []

for _ in range(k):
    arr.append(int(input()))

#랜선을 입력 받고 가장짧은 거:1 
#가장 긴거: 배열중 가장 큰요소로 정한다.
start = 1
end = max(arr)

while start <= end: # end값보다 작거나 같을 때도 포함 주의.
    mid = (start+end)//2
    line = 0
    
    for i in arr:
        line += i // mid #나눠진 랜선 수
    if line >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)