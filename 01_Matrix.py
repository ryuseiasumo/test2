# 隆聖の回答（不正解）
# import numpy as np
#
# H, W, A, B = map(int, input().split())
#
# ans = np.ones((H,W)).astype(np.int64)
#
# for i in range(H):
#     for j in range(W):
#         if i <= B and j <= A:
#             ans[i][j] = 0
#
#         elif i > B and j > A:
#             ans[i][j] = 0
#
#         print(ans[i][j], end="")
#
#         if j != W-1:
#             print(" ", end="")
#
#         if j == W-1:
#             print()



h, w, a, b = [int(j) for j in input().split()]

for i in range(h - b):
    #     print("1")
    print("1" * a + "0" * (w - a))
for i in range(b):
    #     print("2")
    print("0" * a + "1" * (w - a))

