from itertools import combinations

def solution(numbers):
  num_combinations = combinations(numbers, 2)
  result = []
  for combination in num_combinations:
    sum_combi = sum(combination)
    if sum_combi not in result:
      result.append(sum_combi)
    
  
  return sorted(result)

numbers = [5,0,2,7]
print(solution(numbers))