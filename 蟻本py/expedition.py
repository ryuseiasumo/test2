from collections import deque

N = int(input("N = "))
L = int(input("L = "))
P = int(input("P = "))
A = list(map(int, input("A = ").split()))
B = list(map(int, input("B = ").split()))

#ゴールをプライオリティーキュー（もどき）に追加する（距離はN、補給できるガソリンは0）
A.append(L)
B.append(0)

ans = 0
pos = 0
tank = P
que = deque([])

#A[i]を通ったら、B[i]をキューに追加する
for i in range(len(A)):
    d = A[i] - pos
    while tank - d < 0:
        if (len(que) == 0):
            exit("-1")

        tank += que.popleft()
        ans += 1

    que.append(B[i])
    que = deque(sorted(que, reverse = True))
    print(que,pos,tank,ans)
    tank -= d
    pos = A[i]

print(ans)