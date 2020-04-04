N = int(input())
S = input()

if N%2 == 1:
    print("No")

else:
    T = ""
    m = int(N/2)
    for i in range(m):
        T += S[i]

    if T+T in S:
        print("Yes")

    else:
        print("No")