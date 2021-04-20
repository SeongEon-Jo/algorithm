n, k = map(int, input().split())
money = []
ans = 0
for _ in range(n):
    coin = int(input())
    if coin <= k:
        money.append(coin)

money.sort(reverse=True)

for i in range(len(money)):
    if k == 0:
        break

    if money[i] <= k:
        ans += k // money[i]
        k = k % money[i]

print(ans)