import numpy as np

n = int(input("n = "))
time = n
wv_list = [tuple(map(int,input("w v = ").split())) for i in range(time)]
print(wv_list)
W = int(input("W = "))


#非動的計画法での方法
#iはリスト中のi番目の品であること、jはi番目以降の品物の重さの合計がj以下になるようにしないといけないことを表している
# def rec(i, j):
#     if (i == n):
#         print("品切れ")
#         #もう品物は残っていない
#         res = 0
#     elif j < wv_list[i][0]:
#         print(i,"重量オーバー")
#         #この品は入らない
#         res = rec(i + 1, j)
#
#     else:
#         print(i,"追加可能")
#         res = max(rec(i + 1, j),rec(i + 1, j - wv_list[i][0]) + wv_list[i][1])
#
#     return res
#
# print(rec(0,W))


#動的計画法での方法
#再帰関数において、引数が同じ時は返り値も同じ→記憶させておくという方法



dp = np.zeros((n+1,W+1))


def rec(i, j):
    if dp[i][j] > 0:
        print("動的計画法発動！",i,j)
        return dp[i][j]

    if (i == n):
        print("品切れ")
        #もう品物は残っていない
        res = 0
    elif j < wv_list[i][0]:
        print(i,"重量オーバー")
        #この品は入らない
        res = rec(i + 1, j)

    else:
        print(i,"追加可能")
        res = max(rec(i + 1, j),rec(i + 1, j - wv_list[i][0]) + wv_list[i][1])

    dp[i][j] = res
    print(dp)

    return res

print(rec(0,W))
