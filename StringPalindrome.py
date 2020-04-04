S = input()
l = len(S)

flag = True

S_r = S[::-1]

if S != S_r:
    flag = False


s_a = ""
for i in range((l-1)//2):
    s_a += S[i]

s_a_r = s_a[::-1]

if s_a != s_a_r:
    flag = False

s_b = ""
for i in range((l+2)//2,l):
    s_b += S[i]
s_b_r = s_b[::-1]

print(s_a)
print(s_b)

if s_b != s_b_r:
    flag = False

if flag:
    print("Yes")

else:
    print("No")
