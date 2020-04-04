n = int(input())
dict = {}
ans = 0

for i in range(n):
    s = tuple(sorted(input()))
    if s in dict.keys():
        ans += dict[s]
        dict[s] += 1
    else:
        dict[s] = 1
print(ans)

#りゅうせいの解答 オーダーが爆発
# N = int(input())
# s = []
# for i in range(N):
#     s.append(input())
#
# print(s)
#
# ans = 0
#
# while N > 1:
#     for j in range(N-1):   #s[j]とs[N-1]を比べる
#         flag_2 = False
#         while len(s[N-1]):
#             flag = True
#             for k in range(len(s[j])):
#                 if s[N-1][0] == s[j][k]:
#                     s[N-1].lstrip()
#                     s[j].lstrip(s[j][k])
#                     flag = False
#
#             if flag:
#                 flag_2 = True
#                 break
#
#             if (len(s[N-1]) != 0 and len(s[j]) == 0):
#                 flag_2 = True
#                 break
#
#         if flag_2:
#             continue
#
#         elif len(s[j]):
#             continue
#
#         else:
#             ans += 1
#
#     N -= 1
#
# print(ans)