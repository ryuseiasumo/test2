import bisect

N = int(input())
l = list(map(int, input().split()))
l.sort()

ans = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        insert_index = bisect.bisect_left(l, l[i] + l[j],j) #l[i] + l[j]を挿入できる点を探す。同じ者がlにすでにある時は、一番左になるようにする
        ans += (insert_index - j - 1)

print(ans)

#実行時間超過
# N = int(input())
# L_list = list(map(int,input().split()))
# L_list.sort()
# ans = 0
# # print(L_list)
# list = []
# M = 0
#
# for i in range(N-1):
#     for j in range(N-i-1):
#         list.append((L_list[i]+L_list[j+i+1],i,j+i+1))
#         M += 1
# # print(list)
#
#
# for k in range(N):
#     for z in range(M):
#         if L_list[k] < list[z][0]:
#             if (k > list[z][2]):
#                 ans += 1
#
# print(ans)




# 実行時間超過
# for i in range(N-2):
#     J = i+1
#     for x in range(N-i-1):
#         j = J+x
#         K = j+1
#         for y in range(N-j-1):
#             k = K+y
#             if L_list[i] + L_list[j] > L_list[k]:
#                 ans += 1
#             else:
#                 break
#
# print(ans)