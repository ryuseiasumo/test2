from collections import deque

N, Q = map(int, input().split())  # N個の頂点, Q回の操作

# 辺を受け取る
graph = [[] for _ in range(N)]

for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = [0] * N
# その頂点に対して与えられるカウントは伝播する
for i in range(Q):  # Q個の操作について
    p, x = map(int, input().split())
    # ある頂点を根とする部分木には、今現在のcountが全て伝播していく
    count[p-1] += x

q = deque([0])  # 開始のノード
flag = [False] * N

while len(q):
    v = q.pop()
    flag[v] = True  # 部分木の根を到達済みにする

    for e in graph[v]:  # vを根にもつノード全てに操作をする
        # graphは子のみを格納するのではなく、そのノードから出ている辺を
        # 親とか子供とか関係なく全て格納してしまうため、親の方向に
        # 対して伝播をしないようにflagで管理する
        if flag[e]:  # 頂点eがvの親であればスルー
            continue
        # eはvの子供であることが確定する
        count[e] += count[v]  # 親の値を伝播させていく
        q.append(e)

print(*count)

#
# #りゅうせいの解答（実行時エラー）
# import numpy as np
#
# N, Q = map(int,input().split())
#
# ans = []
# for k in range(N):
#     ans.append(0)
#
# #カウント用関数
# def counting(ans,binary_tree,count_list, y, idy):
#     ans[int(binary_tree[idy]) - 1] += y[1]
#     if (binary_tree[idy*2 + 1] != 0):
#         counting(ans, binary_tree, count_list, y, idy*2 + 1)
#
#     if (binary_tree[idy*2 + 2] != 0):
#         counting(ans, binary_tree, count_list, y, idy*2 + 2)
#
#
# #treeの作成
# binary_tree = np.zeros(2**(N+1))
# binary_tree[0] = 1
#
# tuple_list = [list(map(int,input().split())) for i in range(N-1)]
#
# while (len(tuple_list)):
#     x = tuple_list.pop(0)
#     idx = np.where(binary_tree == x[0])[0]
#
#     if (binary_tree[idx*2 + 1] == 0):
#         binary_tree[idx * 2 + 1] = x[1]
#
#     else:
#         binary_tree[idx * 2 + 2] = x[1]
#
# #木の表示
# #print(binary_tree)
#
# count_list = [list(map(int,input().split())) for j in range(Q)]
# while (len(count_list)):
#     y = count_list.pop(0)
#     idy = np.where(binary_tree == y[0])[0]
#     counting(ans, binary_tree, count_list, y, idy)
#
# strs = [str(num) for num in ans]
# print(" ".join(strs))