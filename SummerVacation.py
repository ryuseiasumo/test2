import heapq

# 標準入力受け取り
N, M = list(map(int, input().split()))
jobs = [[] for _ in range(M)]  #日数分(M)だけ[]を用意
# print(jobs)

for i in range(N):
    d, r = list(map(int, input().split()))   #d = A[i], r = B[i]
    if d - 1 < M:   #d-1番目の要素にrを追加して、同じ受け取り日数のバイトを同じ要素に入れる。d-1より、2日後のはjobs[1]におかれる。
        jobs[d - 1].append(-r)  # マイナスにしている
# print(jobs)

rewards = 0
heap = []

# 解法
for i in range(M):
    # 要素を一つづつヒープに追加
    for reward in jobs[i]:
        heapq.heappush(heap, reward)
    # print(heap)
    if len(heap) > 0:
        # 最大値(最小値)をヒープから取り出し
        reward = heapq.heappop(heap)
        rewards += -reward  # マイナスにしている
    # print(heap)

print(rewards)


#りゅうせいの回答（TRE）
# N , M = map(int,input().split())
#
# AB_list =[]
# for i in range(N):
#     AB_list.append(tuple(map(int,input().split())))
#
# AB_list.sort()
# print(AB_list)
# ans = 0
#
# for i in range(M):
#     hoshu = 0
#     t = 0
#     flag = False
#     for j in range(N):
#         if (AB_list[j][0] <= i+1):
#             if hoshu <= AB_list[j][1]:
#                 hoshu = AB_list[j][1]
#                 t = j
#                 flag = True
#
#         else:
#             break
#
#     if flag:
#         del AB_list[t]
#         N -= 1
#     #print(hoshu, t)
#     ans += hoshu
#     #print(AB_list)
#
# print(ans)
