def fibo(n):
  arr = [0] * (n + 1)

  def iterator(n):
    if n <= 2:
      return 1
    
    else:
      if arr[n] == 0:
        arr[n] = iterator(n - 2) + iterator(n - 1)
        return arr[n]
      
      else:
        return arr[n]
  
  return iterator(n)

print(fibo(100))