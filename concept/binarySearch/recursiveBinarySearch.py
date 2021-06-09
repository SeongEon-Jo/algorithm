def binarySearch(arr, target, start, end):
  if start > end:
    return None # 찾는 값 없음
  
  mid = (start + end) // 2

  if arr[mid] == target:
    return mid
  
  elif arr[mid] > target:
    return binarySearch(arr, target, start, mid - 1)
  
  else:
    return binarySearch(arr, target, mid + 1, end)

arr = [1, 3, 5, 6, 8, 13, 19, 20]

print(binarySearch(arr, 20, 0, len(arr) -1))