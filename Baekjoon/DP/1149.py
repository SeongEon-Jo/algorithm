n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n-1):
    arr[i+1][0] += min(arr[i][1], arr[i][2])
    arr[i+1][1] += min(arr[i][0], arr[i][2])
    arr[i+1][2] += min(arr[i][0], arr[i][1])

print(min(arr[n-1]))

# input
# 3
# 26 40 83
# 49 60 57
# 13 89 99