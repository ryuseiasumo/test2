import numpy as np

binary_tree_original = list(map(int,input("元の二分木の要素を入力してください").split()))
pivot = int(input("根にする数を入れてください"))
binary_tree = np.zeros(2 ** len(binary_tree_original))

idx = binary_tree_original.index(pivot)
binary_tree[0] = binary_tree_original.pop(idx)


def binary_tree_maker(bibary_tree, binary_tree_original, a, i):
    print(binary_tree,binary_tree_original,a)

    if a < binary_tree[i]:
        if binary_tree[2 * i + 1] == 0:
            binary_tree[2 * i + 1] = a
        else:
            binary_tree_maker(bibary_tree, binary_tree_original, a, 2 * i + 1)

    else:
        if binary_tree[2 * i + 2] == 0:
            binary_tree[2 * i + 2] = a

        else:
            binary_tree_maker(bibary_tree, binary_tree_original, a, 2 * i + 2)


while len(binary_tree_original) > 0:
    a = binary_tree_original.pop(0)
    binary_tree_maker(binary_tree,binary_tree_original,a,0)

print(binary_tree,binary_tree_original)





