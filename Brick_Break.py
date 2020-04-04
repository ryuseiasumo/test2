N = int(input())
block_list = list(map(int,input().split()))
blocked_list = []

cnt = 1
break_cnt = 0

for i in range(N):
    if block_list[i] == cnt:
        blocked_list.append(cnt)
        cnt += 1

    else:
        break_cnt += 1


if blocked_list == []:
    print(-1)

else:
    print(break_cnt)