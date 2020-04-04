N = 5
S = [1,8,2,6,4]
T = [3,10,5,9,7]

itv = []
for i in range(len(T)):
    itv.append((T[i],S[i]))

itv.sort()
print(itv)

ans = 0
t = 0
for i in range(N):
    if t < itv[i][1]:
        ans += 1
        t = itv[i][0]

print(ans)