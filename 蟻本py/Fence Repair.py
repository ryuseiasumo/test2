
def swap(x,y):
    t = x
    x = y
    y = t
    return (x,y)

N = int(input())
L = list(map(int,input().split()))

ans = 0

#板が1個になるまで適用
while (N > 1):
    mii1 = 0
    mii2 = 1

    #一番短い板mii1、２番目に短い板mii2を求める

    #0番目と1番目を比較
    if (L[mii1] > L[mii2]):
        taple = swap(L[mii1],L[mii2])
        L[mii1] = taple[0]
        L[mii2] = taple[1]
        print(mii1,mii2,"0番目と１番目入れ替え")

    for i in range(2,N):
        # 2番目以降で0番目より小さいのがある場合、それを0番目にして、元々0番目だったのを1番目にする
        if L[i] < L[mii1]:
            mii2 = mii1
            mii1 = i
            print(mii1,mii2,i,"番目の値が0番目に小さい")

        # 2番目以降で1番目より小さいのがある場合、それを1番目にする
        elif L[i] < L[mii2]:
            mii2 = i
            print(mii1,mii2,i,"番目の値が1番目に小さい")

        else:
            print(mii1,mii2,"変更なし")



    #0番目と1番目を併合。tは分割前の状態
    t = L[mii1] + L[mii2]
    ans += t

    #0番目はこの後tに置き換えられるが、0番目が末尾の値の時、N-=1で除外されてしまう。なので、1番目と場所を入れ替えることでtを守る。1番目のが末尾にあってもどうせ除外されるし、末尾にない時は、その時点で末尾にある値に置き換えられるからどうせ除外される
    if (mii1 == N-1):
        taple = swap(mii1,mii2)
        mii1 = taple[0]
        mii2 = taple[1]
        print(mii1,mii2,"末尾が0番目に小さかったので、0番目に小さい値（末尾）と1番目に小さい値の位置を入れ替え")

    print(L,"置き換え直前")
    #小さいの2つを除外し、その2つの和を新しく追加
    L[mii1] = t
    L[mii2] = L[N-1]
    N -= 1
    print(L,"置き換え後")

print(ans)

# りゅうせい解答（誤り）
# N = int(input())
# L = list(map(int,input().split()))
# L.sort()
# cost = 0
# a = len(L)
# for i in range(N-1):
#     for j in range(a):
#         cost += L[j]
#     a -= 1
# print(cost)


