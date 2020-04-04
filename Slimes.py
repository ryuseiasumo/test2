N = int(input())
S = input()
c = '0'
ans = 0

for i in range(N):
    if c == S[i]:
        continue

    elif i == N-1:
        ans += 1

    else:
        c = '0'

        if S[i] == S[i+1]:
            c = S[i]
            ans += 1

        else:
            ans += 1

print(ans)