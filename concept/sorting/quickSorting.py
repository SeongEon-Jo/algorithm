arr = [3, 1, 9, 2, 11, 13, 6, 8]

# 개념 : pivot을 기준으로 왼쪽에서부터 arr[pivot]보다 큰 값을, 맨 끝에서부터 arr[pivot]보다 작은 값을 서치
# 엇갈리지 않을 경우 - arr[left] arr[right] Swap
# 엇갈릴 경우 - arr[right]과 arr[pivot] Swap -> 이러면 pivot을 기준으로 arr[pivot]보다 작은 값이 왼쪽, 큰 값이 오른쪽으로 정렬

def quickSorting(arr, start, end):
  if  start >= end:
    return
  
  pivot = start
  left = start + 1
  right = end

  while left <= right:
    while left <= end and arr[left] <= arr[pivot]:
      left += 1
    
    while right > start and arr[right] >= arr[pivot]:
      right -= 1

    if left > right:
      arr[right], arr[pivot] = arr[pivot], arr[right]
    
    else:
      arr[left], arr[right] = arr[right], arr[left]

  # 엇갈린 후, arr[pivot]과 arr[right]을 swap 하면, pivot 인덱스는 right 인덱스가 됨
  quickSorting(arr, start, right-1)
  quickSorting(arr, right+1, end)

quickSorting(arr, 0, len(arr)-1)
print(arr)