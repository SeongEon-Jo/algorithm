from collections import deque
def bfs(graph, start, visited):
  visited[start] = True
  queue = deque([start])

  while queue:
    current = queue.popleft()
    print(current, end=' ')

    for i in graph[current]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)