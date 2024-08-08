import sys
from collections import deque
#요세푸스 문제0

n,k = map(int,input().split())
Q = deque()
res = []

for i in range(1,n+1):  #1부터 n까지 큐에 집어넣는다.
    Q.append(i)
    
while Q:
    for i in range(k-1): #k-1번동안 맨 앞 요소를 꺼내서 맨 뒤에 다시 추가.
        Q.append(Q.popleft()) #k=3이라면, 1,2를 빼서 맨 뒤에 다시 추가한다.
    res.append(Q.popleft()) #k=3이라면, 맨 앞의 3을 결과를 저장할 배열에 다시 넣는다.

list_res = str(res)[1:-1]
print('<' + list_res + '>')