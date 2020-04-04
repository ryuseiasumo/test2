M, D = map(int,input().split())

count = 0
for m in range(M+1):
    for d in range(D+1):
        d_1 = d % 10
        d_10 = d // 10
        if (d_10 >= 2 and d_1 >= 2 and m == d_10*d_1):
            print(m, d_10, d_1)
            count += 1

print(count)