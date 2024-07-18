from collections import deque

n = int(input()) #컴퓨터 개수
v = int(input()) #연결된 수
graph = [[] for i in range(n+1)]
visited = [0]*(n+1)
#그래프 초기화 + 방문했는지 여부 확인
cnt = 0

for _ in range(v):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x) #양방향으로 두 노드를 연결

def bfs(v):
    global cnt
    visited[v] = 1
    queue = deque([v])
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                cnt += 1
    return cnt

print(bfs(1))