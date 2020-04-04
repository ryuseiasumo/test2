N = int(input())

d_list = list(map(int,input().split()))
ans = 0

for i in range(N):
    for j in range(N):
        if (i != j):
            kaihuku = d_list[i]*d_list[j]
            ans += kaihuku

print(int(ans/2))