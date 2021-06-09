def binarySearch(arr, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if arr[mid] == target:
      return mid
    
    elif arr[mid] > target:
      end = mid - 1
    
    else:
      start = mid + 1
  
  return None

arr = [1, 3, 5, 6, 8, 13, 19, 20]
print(binarySearch(arr, 3, 0, len(arr)-1))