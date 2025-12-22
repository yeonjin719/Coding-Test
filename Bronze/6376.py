print("n e")
print("- -----------")
dp = []
dp.append(1)
factorial = 1
for N in range(1, 10):
  factorial *= N
  dp.append((1/(factorial)) + dp[N-1])  

for i in range(len(dp)):
  if dp[i] == int(dp[i]):
    print(i, f"{int(dp[i])}")
  elif dp[i] == float(f"{dp[i]:.1f}"):
    print(i, f"{dp[i]:.1f}")
  else:
    print(i, f"{dp[i]:.9f}")