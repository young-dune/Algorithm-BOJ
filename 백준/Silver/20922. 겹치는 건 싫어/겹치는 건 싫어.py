import sys
input=sys.stdin.readline

n,k = map(int,input().split()) #n: 배열길이, k:같은 숫자 나올 수 있는 최대 횟수
arr = list(map(int,input().split()))
cnt = 100001*[0] #해당 숫자가 몇 번 나왔는지 체크
start,end,result = 0,0,0 
#시작점, 끝점, 결과값

while end < n: #끝점이 n미만일 때까지만 반복
    if cnt[arr[end]] < k: 
        cnt[arr[end]] += 1 
        end += 1 
    else: 
        cnt[arr[start]] -= 1 
        start +=1 
    result = max(result,end-start) #while문 안에서 최대값 비교후 갱신
print(result)

