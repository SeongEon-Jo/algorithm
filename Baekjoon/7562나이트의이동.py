from collections import deque

dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]

def bfs(start_x, start_y, target_x, target_y):
  q = deque()
  q.append((start_x, start_y))

  graph[start_x][start_y] = 1

  while q:
    x, y = q.popleft()

    for i in range(8):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] == 0:
          graph[nx][ny] = graph[x][y] + 1
          if nx == target_x and ny == target_y:
            return graph[nx][ny] - 1
          q.append((nx, ny))


t = int(input())
ans_list = []
for _ in range(t):
    n = int(input())
    start_x, start_y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    graph = [[0] * n for _ in range(n)]

    ans_list.append(bfs(start_x, start_y, target_x, target_y))

for x in ans_list:
    if x == None:
        print(0)
    else: print(x)
