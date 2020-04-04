N, K, Q = map(int,input().split())

A_list = [int(input()) for i in range(Q)]
Point_list = [K-Q for i in range(N)]

for j in range(Q):
    Point_list[A_list[j]-1] += 1

for j in range(N):
    if Point_list[j] <= 0:
        print("No")

    else:
        print("Yes")

