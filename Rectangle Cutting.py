# #りゅうせいの解答（間違っている）
# w, h, x, y, *yobun = [i for i in map(int,input().split())]
#
# if (w < 1 or 10**9 < h):
#     print("Wは１以上,Hは10^9以下にしてください")
#     exit(1)
# elif (x < 0 or w < x):
#     print("0 <= x <= W にしてください")
#     exit(1)
#
# elif (y < 0 or h < y):
#     print("0 <= y <= H にしてください")
#     exit(1)
#
# s = []
# for i in range(w+1):
#     for j in range(y+1):
#         if (i == x):
#             if (j != y):
#                 s.append(min(h * x, h * (w-x)))
#
#         else:
#             a = (y - j) / (x - i)
#             b = y - a * x
#             l = y + a * (w - x) #直線のx座標がwの時のy座標
#
#             if b >= 0:
#                 if l >= y:
#                     if a == 0 and b == 0:
#                         s.append(0)
#                     elif a == 0:
#                         s.append(min(b * w , (h-b) * w ))
#                     else:
#                         x = (h - b) / a
#                         s.append(1/2 * (h-b) * x)
#
#                 elif l <= 0:
#                     # if a == 0:
#                     #     s.append(0)
#                     # else:
#                         x = -b / a
#                         s.append(1/2 * b * x)
#
#                 else:
#                     s.append(min( 1/2 * (b + l) * w , 1/2 * ((h-b)+(h-l)) * w ))
#
#             else:
#                 x = -b / a
#                 if l <= h:
#                     s.append(1/2 * l * (w - x))
#                 else:
#                     z = (h - b) / a
#                     s.append(min(1/2 * (x+z) * h, 1/2 * ((w - x) + (w - z)) * h))
# print(s)
# s_max = max(s)
# kosu = [i for i, x in enumerate(s) if x == s_max]
# if (len(kosu) == 1):
#     print(s_max, "0")
# else:
#     print(s_max, "1")
#
#
# W, H, x, y = map(int, input().split())

#正解
W, H, x, y = map(int, input().split())

# 面積は必ず二等分可能
# 面積を二等分する直線は長方形の中心を通る
ans = '{} {}'.format(
    W * H / 2,
    1 if x == W / 2 and y == H / 2 else
    0
)

# 出力
print(ans)