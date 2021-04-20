n = int(input())
num_list = []
for _ in range(n):
  num_list.append(int(input()))

def solution(num):
  if num == 0:
    return 0
  
  if num == 1:
    return 1
  
  if num == 2:
    return 2
  
  if num == 3:
    return 3

  else:
    return solution(n-3) + solution(n-2) + solution(n-1)

for x in num_list:
  print(solution(x))