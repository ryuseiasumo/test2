import copy
N = int(input())
a_list = list(map(int,input().split()))

b_list = sorted(a_list)

for i in range(N):
    c_list = copy.copy(b_list)
    c_list.remove(a_list[i])

    ans = 0
    t = 0
    count = 0

    for j in range(N-1):
        if t == c_list[j]:
            count += 1
        else:
            t = c_list[j]
            ans += int(count*(count-1)/2)
            count = 1
    ans += int(count*(count-1)/2)

    print(ans)
