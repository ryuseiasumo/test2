N = int(input())
X = list(map(int,input().split()))
R = int(input())

i = 0
ans = 0

while i < N:
    s = X[i]
    while (i < N and X[i] <= s + R):
        i += 1

    p = X[i-1]
    while (i < N and X[i] <= p + R):
        i += 1

    print(s,p,ans)

    ans += 1

print(ans)