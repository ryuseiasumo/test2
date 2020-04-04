import heapq
N = int(input())

A_list = list(map(int, input().split()))

# ans = [A_list.index(i+1)+1 for i in range(N)]
#
# for i in range(N):
#     print(ans[i], end=" ")

list = [(A_list[i],i+1) for i in range(N)]
heapq.heapify(list)

for i in range(N):
    print(heapq.heappop(list)[1], end=" ")
