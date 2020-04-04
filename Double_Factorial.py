n=int(input())
if n%2!=0:
    print(0)
else:
    n=n//2
    ans=0
    while n:
        ans+=n//5
        n=n//5
    print(ans)

#
# def solve(x, keta):
#     cnt = 0
#     jou = 0
#     while keta > 0:
#         cnt += (keta-1) * (9 ** jou)
#         keta -= 1
#         jou += 1
#
#     # print(x*cnt)
#     return x*cnt
#
# N = int(input())
# ans = 0
#
# if N%2 == 1:
#     print(0)
#
# else:
#     keta = len(str(N))
#     # print(keta,"\n")
#
#     while(keta > 0):
#         x = N//(10**(keta-1))
#         # print(x)
#         # print(keta)
#
#         ans += solve(x, keta)
#
#         N -= x*(10**(keta-1))
#         keta -= 1
#         # print()
#
#     print(ans)