from collections import deque

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()
for i in range(n):
  for j in range(m):
    if arr[i][j] == 1:
      # 시작점 기록
      q.append((i, j))

while q:
  x, y = q.popleft()
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < n and 0 <= ny < m:
      if arr[nx][ny] == 0:
        q.append((nx, ny))
        arr[nx][ny] = arr[x][y] + 1

ans = -1
for i in range(n):
  if 0 in arr[i]:
    ans = -1
    break
  
  else:
    ans = max(ans, max(arr[i]))

if ans == -1:
  print(-1)

else:
  print(ans-1)