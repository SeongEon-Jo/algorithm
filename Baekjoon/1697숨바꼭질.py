from collections import deque

N, K = map(int, input().split())
visited = [False] * 100001

def bfs(v):
  count = 0
  q = deque()
  q.append([v, count])

  while q:
    x = q.popleft()
    current, count = x[0], x[1]
    if visited[current] == False:
      visited[current] = True
      if current == K:
        return count
      
      count += 1
      
      if current * 2 <= 100000:
        q.append([current * 2, count])
      
      if current + 1 <= 100000:
        q.append([current + 1, count])
      
      if current - 1 >= 0:
        q.append([current - 1, count])

  return count

print(bfs(N))