import heapq
n,m = map(int,input().split())
q = [[] for i in range(m)]

for i in range(n):
  a,b = map(int,input().split())
  a -= 1
  if a < m:
    heapq.heappush(q[a],-b)

a = 0
cur = []
for i in range(m):
  for j in q[i]:
    heapq.heappush(cur,j)
  if cur:
    a += heapq.heappop(cur)
print(-a)


# りゅうせいの解答 実行時間超過、不正解
# N, M = map(int, input().split())
#
# work_list = [list(map(int,input().split())) for i in range(N)]
# work_list.sort()
#
# sum = 0
# for j in range(M+1):
#     hoshu = 0
#     t = N+1
#     k = 0
#
#     while (k <= N-1 and work_list[k][0] <= j):
#         hoshu = max(hoshu, work_list[k][1])
#         t = k
#         k += 1
#     sum += hoshu
#
#     if t != N+1:
#         del work_list[t]
#         N -= 1
#
# print(sum)
#
