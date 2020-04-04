N ,K = map(int,input().split())

M_list = []

#とりあえず輪にしてから内部で繋いでみる？
if N < K:
    for i in range(N-1):
        M_list.append([i+1, i+2])
    M_list.append([N,1])

print(M_list)



