import numpy as np

n = int(input("n = "))
wv_list = [tuple(map(int,input("w v = ").split())) for i in range(n)]
W = int(input(" W = "))

dp = np.zeros((n+1,W+1))

# りゅうせい解答（間違っている）
# for i in range(n):
#     for j in range(W+1):
#         if j < wv_list[i][0] :
#             dp[i+1][j] = dp[i][j]
#
#         elif i+1 < n:
#             dp[i+1][j] = max(dp[i][j],dp[i][j-wv_list[i][0]] + wv_list[i][1], dp[i+1][j - wv_list[i+1][0]] + wv_list[i+1][1])
#
#         else:
#             print(i,j)
#             dp[i + 1][j] = max(dp[i][j], dp[i][j - wv_list[i][0]] + wv_list[i][1])
#
# print(dp)
# print(dp[n][W])


#解答1（pythonでは実装不可？？）
# for i in range(n):
#     for j in range(W+1):
#         for k in range(k * wv_list[i][0]<=j):
#             dp[i+1][j] = max(dp[i+1][j],dp[i][j - k*wv_list[i][0]] + k * wv_list[i][1])
#
# print(dp[n][W])


#