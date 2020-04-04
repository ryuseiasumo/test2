N = int(input())
B_list = list(map(int,input().split()))

A = 0
for i in range(N-1):
    if i == 0:
        A += B_list[0]
    else:
        A += min(B_list[i-1],B_list[i])

A += B_list[N-2]
print(A)