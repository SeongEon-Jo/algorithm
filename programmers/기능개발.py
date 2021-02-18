from collections import deque

def solution(progresses, speeds):
  answer = []
  progresses = deque(progresses)
  speeds = deque(speeds)

  while progresses:
    while progresses[0] < 100:
      for i in range(len(progresses)):
        progresses[i] += speeds[i]

    cnt = 0 
    while progresses:
      if progresses[0] >= 100:
        cnt += 1
        progresses.popleft()
        speeds.popleft()

      else:
        break

    answer.append(cnt)

  return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))