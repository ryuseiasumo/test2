N = int(input())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))
C_list = list(map(int,input().split()))

satisfaction = 0

for i in range(N):
    satisfaction += B_list[A_list[i] - 1]
    if (i != N-1 and A_list[i + 1] == A_list[i] + 1):
        satisfaction += C_list[A_list[i]-1]

print(satisfaction)