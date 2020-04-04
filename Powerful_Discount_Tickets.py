import heapq

N, M = map(int, input().split())
A_heap = list(map(lambda x: int(x)*(-1), input().split()))
heapq.heapify(A_heap)

ans = 0

for i in range(M):
    x = heapq.heappop(A_heap) * (-1)
    heapq.heappush(A_heap, int(x/2) * (-1))

for i in range(N):
    ans -= A_heap[i]

print(ans)