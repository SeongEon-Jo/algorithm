from collections import deque

N, M = map(int, input().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

# bfs
def bfs(v):
  q = deque()
  q.append(v)

  while q:
    x = q.popleft()
    if visited[x] == False:
      visited[x] = True

      for i in graph[x]:
        q.append(i)

def dfs(v):
  visited[v] = True
  for i in graph[v]:
    if visited[i] == False:
      dfs(i)

cnt = 0
for i in range(1, N+1):
  if visited[i] == False:
    bfs(i)
    cnt += 1

print(cnt)