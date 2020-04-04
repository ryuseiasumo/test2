from collections import deque

N = int(input("N = "))
L = list(map(int,input("L = ").split()))

ans = 0

que = deque([])
for i in range(N):
    que.append(L[i])


while len(que) > 1:
    que = deque(sorted(que))
    print(que)
    l1 = que.popleft()
    l2 = que.popleft()
    print(que)
    ans += l1 + l2
    que.append(l1 + l2)

print(ans)