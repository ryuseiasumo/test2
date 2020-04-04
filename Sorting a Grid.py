import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

"""
正則二部グラフの辺彩色
"""

import numpy as np

N, M = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(N)]

edge = []
for i, row in enumerate(grid):
    for j, x in enumerate(row):
        edge.append(((x - 1) // M, N + i))

graph = [dict() for _ in range(N + N)]  # 頂点ごろに、色->相手
rest_color = [set(range(M)) for _ in range(N + N)]

for u, v in edge:
    common = rest_color[u] & rest_color[v]
    if common:
        c = common.pop()
        graph[u][c] = v
        graph[v][c] = u
        rest_color[u].remove(c)
        rest_color[v].remove(c)
        continue
    # 交互道を作って色c,dと当てていく
    c = rest_color[u].pop()
    d = rest_color[v].pop()
    cd = c + d
    V = [u, v]
    next_c = c
    while next_c not in rest_color[v]:
        v = graph[v][next_c]
        V.append(v)
        next_c = cd - next_c
    rest_color[v].remove(next_c)
    rest_color[v].add(cd - next_c)
    for i, (u, v) in enumerate(zip(V, V[1:])):
        if i % 2 == 0:
            graph[u][c] = v
            graph[v][c] = u
        else:
            graph[u][d] = v
            graph[v][d] = u

after = [[None] * M for _ in range(N)]

for i, row in enumerate(grid):
    mod_to_x = [[] for _ in range(N)]
    for x in row:
        mod_to_x[(x - 1) // M].append(x)
    for color in range(M):
        after[i][color] = mod_to_x[graph[i + N][color]].pop()

B = np.array(after)
C = B.copy()
C.sort(axis=0)
print('\n'.join(' '.join(row) for row in B.astype(str)))
print('\n'.join(' '.join(row) for row in C.astype(str)))
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

"""
正則二部グラフの辺彩色
"""

import numpy as np

N, M = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(N)]

edge = []
for i, row in enumerate(grid):
    for j, x in enumerate(row):
        edge.append(((x - 1) // M, N + i))

graph = [dict() for _ in range(N + N)]  # 頂点ごろに、色->相手
rest_color = [set(range(M)) for _ in range(N + N)]

for u, v in edge:
    common = rest_color[u] & rest_color[v]
    if common:
        c = common.pop()
        graph[u][c] = v
        graph[v][c] = u
        rest_color[u].remove(c)
        rest_color[v].remove(c)
        continue
    # 交互道を作って色c,dと当てていく
    c = rest_color[u].pop()
    d = rest_color[v].pop()
    cd = c + d
    V = [u, v]
    next_c = c
    while next_c not in rest_color[v]:
        v = graph[v][next_c]
        V.append(v)
        next_c = cd - next_c
    rest_color[v].remove(next_c)
    rest_color[v].add(cd - next_c)
    for i, (u, v) in enumerate(zip(V, V[1:])):
        if i % 2 == 0:
            graph[u][c] = v
            graph[v][c] = u
        else:
            graph[u][d] = v
            graph[v][d] = u

after = [[None] * M for _ in range(N)]

for i, row in enumerate(grid):
    mod_to_x = [[] for _ in range(N)]
    for x in row:
        mod_to_x[(x - 1) // M].append(x)
    for color in range(M):
        after[i][color] = mod_to_x[graph[i + N][color]].pop()

B = np.array(after)
C = B.copy()
C.sort(axis=0)
print('\n'.join(' '.join(row) for row in B.astype(str)))
print('\n'.join(' '.join(row) for row in C.astype(str)))
