import heapq

def minus(x):
    y = int(x)
    return y*(-1)

N , K = map(int,input().split())
h_list = list(map(minus,input().split()))
ans = 0
heapq.heapify(h_list)

for i in range(N):
    if (heapq.heappop(h_list)*(-1) < K):
        break

    else:
        ans += 1


print(ans)
