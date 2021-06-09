def merge(list1, list2):
  merged_list = []
  i = 0
  j = 0

  while i < len(list1) and j < len(list2):
    if list1[i] > list2[j]:
      merged_list.append(list2[j])
      j += 1
    
    else:
      merged_list.append(list1[i])
      i += 1

  if i == len(list1):
    for x in range(j, len(list2)):
      merged_list.append(list2[x])
  
  else:
    for x in range(i, len(list1)):
      merged_list.append(list1[x])
  
  return merged_list

def merge_sort(li):
  if len(li) < 2:
    return li

  return merge(
    merge_sort(li[:len(li)//2]),
    merge_sort(li[len(li)//2:])
  )

arr = [3, 1, 9, 2, 11, 13, 6, 8]
print(merge_sort(arr))