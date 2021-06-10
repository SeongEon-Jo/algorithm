def bubbleSorting(arr):
  for i in range(len(arr)-1, 0, -1):
    for j in range(i):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

  return arr

arr = [3, 1, 9, 2, 11, 13, 6, 8]
print(bubbleSorting(arr))