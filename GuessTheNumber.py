a = [-1, -1, -1]

def search():
    for i in range(M):
        s, c = map(int, input().split())
        if N == 3 and s == 1 and c == 0:
            return False

        if N == 2 and s == 1 and c == 0:
            return False

        if a[s-1+3-N] != -1 and a[s-1+3-N] != c:
            return False

        a[s-1+3-N] = c

    return True


N ,M = map(int, input().split())

if search():
    if a[2] == -1:
        a[2] = 0

    if a[1] == -1:
        if N == 2:
            a[1] = 1
        else:
            a[1] = 0

    if a[0] == -1:
        if N == 3:
            a[0] = 1
        else:
            a[0] = 0



    ans = a[0]*100 + a[1]*10 + a[2]
    print(ans)

else:
    print(-1)
