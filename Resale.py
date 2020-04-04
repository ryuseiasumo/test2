N = int(input())
V_list = list(map(int,input().split()))
C_list = list(map(int,input().split()))

sum = 0
for i in range(N):
    v = V_list[i] - C_list[i]
    if (v > 0):
        sum += v

print(sum)