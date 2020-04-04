N = int(input())
H = list(map(int, input().split()))

ans = 0

count = 0
for i in range(N-1):
    if (H[N-1-i] <= H[N-2-i]):
        count += 1
        if i == N-2:
            ans = max(ans, count)

    else:
        ans = max(ans, count)
        count = 0

print(ans)