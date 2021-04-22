def solution(board, moves):
  ans = 0
  picked = []
  for move in moves:
    for i in range(len(board)):
      if board[i][move - 1] != 0:
        picked.append(board[i][move-1])
        board[i][move-1] = 0
        break
    
    if len(picked) > 1:
      if picked[-1] == picked[-2]:
        picked.pop()
        picked.pop()
        ans += 2

  return ans

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))