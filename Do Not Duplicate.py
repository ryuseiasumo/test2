N, K = map(int,input().split())
A = list(map(int,input().split()))
s = []

for i in range(N*K):
    j = i % N
    if (A[j] in s):
        d = s.index(A[j])
        del s[d:]

    else:
        s.append(A[j])

print(" ".join(map(str, s)))

