while True:
  n, maxAmount = input().split()
  n = int(n)
  maxAmount = int(float(maxAmount)*100+0.5)
  if n==0 and maxAmount==0:
      break

  lists = []

  for _ in range(n):
      a, b = input().split()
      a = int(a)
      b = int(float(b)*100+0.5)
      lists.append([a,b])

  dp = [0]*10001

  for cal, cost in lists:
      for i in range(cost, maxAmount+1):
          dp[i] = max(dp[i-cost] + cal, dp[i])
  print(dp[maxAmount])