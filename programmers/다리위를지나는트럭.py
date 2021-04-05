def solution(bridge_length, weight, truck_weights):
  answer = 0 
  queue = [0] * bridge_length

  while queue:
    answer += 1
    queue.pop(0)

    if truck_weights:
      if weight >= sum(queue) + truck_weights[0]:
        queue.append(truck_weights.pop(0))

      else:
        queue.append(0)

  return answer

  print(solution(2, 10, [7, 4, 5, 6]))
  print(solution(100, 100, [10]))
  print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))