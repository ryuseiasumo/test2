# import math
#
# A, B, C = map(int,input().split())
# X = int(input())
#
#
# # 100円4枚、50円1枚は残して残りは500円として扱えるだけ扱う
# b = C//2
# C = C-2*b
#
# print(C)
#
# if (X%100 == 50):
#     if b == 0:
#         print(0)
#         exit(1)
#     #cnt_C = 2になる。他はcnt_C=1
#     elif C == 0:
#         C = 2
#         b -= 1
#
# #100円玉扱いの枚数
# B += b
# a = B//5
# B = B-5*a
#
# if (X%500 > 100*B):
#     if a == 0:
#         print(0)
#         exit(1)
#     else:
#         B += 5
#         a -= 1
#
# #500円玉扱いの枚数
# A += a
#
# if (A < X//500):
#     print(0)
#
# else:
#     m = X//500
#     if m == 0:
#         cnt_A = 1
#     else:
#         cnt_A = math.factorial(A)/(math.factorial(A-m)*math.factorial(m))
#
#     n = (X%500)//100
#     if n == 0:
#         cnt_B = 1
#     else:
#         cnt_B = math.factorial(B)/(math.factorial(B-n)*math.factorial(n))
#
#     if C == 0:
#         cnt_C = 1
#
#     else:
#         cnt_C = C
#
#     ans = cnt_A*cnt_B*cnt_C
#     print(ans)