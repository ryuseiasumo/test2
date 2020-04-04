N = int(input())
S = input()
mod = 10 ** 9 + 7

LR = ["0" for j in range(2*N)]
LR[0] = "L"
LR[N-1] = "R"

ans = 0
cnt_r = 0
cnt_l = 0

if S[0] == "W" or S[2*N-1] == "W":
    print(0)

else:
    i = 0
    while i < 2*N-i:
        if S[i] == S[i+1]:
            if LR[i] == "L":
                LR[i+1] = "R"
            else:
                LR[i+1] = "L"

        else:
            LR[i+1] = LR[i]

        if S[2*N-i-1] == S[2*N-i-2]:
            if LR[2*N-i-1] == "L":
                LR[2*N-i-2] = "R"
            else:
                LR[2*N-i-2] = "L"
        else:
            LR[2*N-i-2] = LR[2*N-i-1]

        i += 1
    # else:
    #     if (i == N-i-1):
    #         if (S[i-1] == S[N-i]):
    #             print(0)
    #
    #         else:
    #             print(ans)


    print(LR)

