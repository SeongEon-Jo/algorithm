# 정렬되지 않은 배열
arr = [3, 1, 9, 2, 11, 13, 6, 8]

def selectionSorting(arr):
  for i in range(len(arr)):
    min_index = i

    for j in range(i+1, len(arr)):
      if arr[min_index] > arr[j]:
        min_index = j
    
    if min_index != i:
      arr[min_index], arr[i] = arr[i], arr[min_index]

  return arr

print(selectionSorting(arr))