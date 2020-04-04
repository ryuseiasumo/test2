N = int(input())
s_list = []
s_dict = {}
ans = 0

for j in range(N):
    s_list.append("".join(sorted(input())))

for i in range(N):
    if s_list[i] in s_dict.keys():
        ans += s_dict[s_list[i]]
        s_dict[s_list[i]] += 1

    else:
        s_dict[s_list[i]] = 1

print(ans)

