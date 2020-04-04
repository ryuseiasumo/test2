import numpy as np

n = int(input("n = "))
m = int(input("m = "))
s = input("文字列 s = ")
t = input("文字列 t = ")

dp = np.zeros((n+1,m+1))

for i in range(n):
    for j in range(m):
        if (s[i] == t[j]):
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j+1],dp[i+1][j])

print(dp[n][m])
