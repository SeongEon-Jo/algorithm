arr = [3, 1, 9, 2, 11, 13, 6, 8]

def insertionSorting(arr):
  for i in range(1, len(arr)):
    for j in range(i, 0, -1):
      if arr[j] < arr[j-1]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
      
      else:
        break

  return arr

print(insertionSorting(arr))