N = int(input())

mod_sum = N*(N-1)//2
print(mod_sum)

#りゅうせいの解答2 不正解2つあり
# N = int(input())
#
# mod_sum = int(N*(N-1)/2)
# print(mod_sum)

# りゅうせいの解答1　実行時間超過
#  N = int(input())
#
# P_list = []
# M_list = []
#
#
# for i in range(N):
#     if i == N-1:
#         P_list.append(1)
#
#     else:
#         P_list.append(i+2)
#
#
# for i in range(N):
#     M_list.append((i+1) % P_list[i])
#
# print(sum(M_list))