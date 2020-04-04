S = input()
N = len(S)

flag = False
for i in range(N):
    if i%2 == 0:
        if S[i] == "L":
            flag = True
            break

    else:
        if S[i] == "R":
            flag = True
            break

if flag:
    print("No")

else:
    print("Yes")
