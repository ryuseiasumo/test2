N ,X = map(int,input().split())
a_list = list(map(int,input().split()))
a_list.sort(reverse=True)

max = a_list[0]
kagen = max - X

ans = 0
for i in range(N):
    if a_list[i] < kagen:
        break
    else:
        ans += 1

print(ans)
