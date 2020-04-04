K, X = map(int, input().split())

min = X - (K - 1)

for i in range(2*K-1):
    print(min + i)