N = int(input())

S,T = input().split()

# print(S)
# print(T)

ans = ""

for i in range(N):
    ans += S[i]
    ans += T[i]

print(ans)