def solution(N, stages):
  ans = {}
  player_num = len(stages)
  for x in range(1, N+1):
    # 1단계 통과 (2단계 통과 X)
    notclear = stages.count(x)
    ans[x] = notclear / player_num
    player_num -= notclear

  return sorted(ans, key = lambda x: ans[x], reverse=True)

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))