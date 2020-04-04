
#りゅうせいの解答
# n, k = map(int,input().split())
# a = list(map(int, input().split()))
#
# cnt = 0
# for i in range(n):
#     sum_a = 0
#     for j in range(i,n,+1):
#         sum_a += a[j]
#         if sum_a >= k:
#             cnt += 1
#
# print(cnt)
#

#しゃくとり法の解答
n, k = map(int, input().split())    #NとK
a = list(map(int, input().split()))  #配列A

i = 0
j = 0
sm = 0
ans = 0  #Kをsmが超えている回数
while j < n:   #jがnより小さい間（NはAの要素数）
    sm = sm + a[j]  #最終的に、sm = a[0]+a[1]+...+a[n-1]
    while sm >= k and i < n: #smがKを超えていて、かつ、iがnより小さい
        ans = ans + (n - j)  #a[i]からa[j]までの和がKを超えてるなら、a[i]からa[j]以降までの和も全てKを超えている。すなわちn-j個超えているものがある
        sm = sm - a[i]  #最初はsm-a[0]、すなわちa[1]+...+a[j]
        i += 1
        print(sm, ans)
    j += 1

    print(sm,ans)
print(ans)



