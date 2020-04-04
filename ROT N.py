S = input()
N = int(input())
n = int(N%26)

l = len(S)
i = 0
ans = ''

while l:
    if S[i] == 'z':
        tmp = S.replace(S[i],chr(ord('a') + n - 1))
    else:
        tmp = S.replace(S[i],chr(ord(S[i])+ n))
    ans += tmp[i]
    i += 1
    l -= 1

print(ans)