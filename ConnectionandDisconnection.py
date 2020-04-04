S = input()
K = int(input())

S = S*K
cnt = 0
flag = False

for i in range(len(S)-1):
    if flag:
        flag = False

    else:
        if S[i] == S[i+1]:
            cnt += 1
            flag = True

print(cnt)