#考え方
#（BについてCでもDでも割り切れない数の個数）-（についてCでもDでも割り切れない数の個数）
#↑それぞれは、B -（B//C + B//D - B//lcm(C,D)) 、　A -（A//C + A//D - A//lcm(C,D))で出せる

def gcd(x, y):
    if x%y == 0:
        return y

    else:
        return gcd(y,x%y)



A, B, C, D = map(int,input().split())

if C < D:
    t = C
    C = D
    D = t

max_ky = gcd(C,D)

#最小公倍数
lcm_c = C//max_ky
lcm_d = D//max_ky
lcm = max_ky * lcm_c * lcm_d
count_b = B - (B//C + B//D - B//lcm)
count_a = A - (A//C + A//D - A//lcm)
if(A%C != 0 and A%D != 0):
    count_a -= 1
ans = count_b - count_a

print(ans)






#りゅうせいの解答1 実行時間超過
#A, B, C, D = map(int,input().split())
# ans = 0
# j = A
# while j <= B:
#     count = 0
#     if j%C:
#         count += 1
#     if j%D:
#         count += 1
#
#     if count == 2:
#         ans += 1
#
#     j+= 1
#
# print(ans)


