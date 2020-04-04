import copy

N, K = map(int, input().split())
original = list(map(int,input().split()))
list_sort = []
cnt = 0

for i in range(N-K+1):
    after = copy.deepcopy(original)
    after_pre = original
    after[i:i+K] = sorted(after_pre[i:i+K])

    if after in list_sort:
        continue
    else:
        list_sort.append(after)
        cnt += 1


print(list_sort)
print(cnt)



