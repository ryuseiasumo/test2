# 必要なモジュールの読み込み
import numpy as np
import math

# 学習率
eta = 0.1
rho = 1

# データの読み込み
#xに入力、yに教師信号
x = np.array([[0,0,-1], [1,0,-1], [0,1,-1], [1,1,-1]])
y = np.array([[0],[1],[1],[0]])

#試行回数
cnt = 1

# 重みの初期化はランダムにしておく
w1 = np.random.randn(2, 3) # 中間層の数，入力＋1
w2 = np.random.randn(1, 3) # 出力, 中間層+1
print(w1)
print(w2)

while (1):
    # print(cnt, "回目")
    print(cnt, "回目")
    print(w1)
    print(w2)

    cnt += 1
    count_1 = 0
    for n in range(len(x)):
        M = len(x[0])
        h1 = np.array([0.0, 0.0])
        for j in range(len(h1)):
            for i in range(M):
                h1[j] += x[n][i] * w1[j][i]

        g1 = np.array([0.0, 0.0])
        for j in range(len(h1)):
            g1[j] = 1 / (1 + math.exp(-h1[j]))  # シグモイド関数
        g1 = np.hstack((g1, -1))

        N = len(y[0])
        h2 = np.zeros(N)
        for k in range(len(h2)):
            for j in range(len(g1)):
                h2[k] += g1[j] * w2[k][j]

        g2 = np.zeros(N)
        for k in range(len(h2)):
            g2[k] = 1 / (1 + math.exp(-h2[k]))  # シグモイド関数

        # print(g2)
        count_2 = 0
        for i in range(len(g2)):
            if (g2[i] <= eta or g2[i] >= 1 - eta):
                count_2 += 1
        if (count_2 == len(g2)):
            count_1 += 1

        ep2 = np.zeros(N)
        for j in range(N):
            ep2[j] = (g2[j] - y[n][j]) * g2[j] * (1 - g2[j])

        ep1 = np.zeros(len(g1))
        for j in range(len(g1)):
            a = 0
            for k in range(N):
                a += ep2[k] * w2[k][j]
            ep1[j] = a * g1[j] * (1 - g1[j])

        for i in range(len(w1[0])):
            for j in range(len(h1)):
                w1[j][i] = w1[j][i] - rho * ep1[j] * x[n][i]

        for i in range(len(w2[0])):
            for j in range(N):
                w2[j][i] = w2[j][i] - rho * ep2[j] * g1[i]

    if (count_1 == len(x)):
        break

print(cnt, "回目")
print(w1)
print(w2)

test_x = np.array([[0, 0, -1], [1, 0, -1], [0, 1, -1], [1, 1, -1]])
test_y = np.array([[0], [1], [1], [0]])

# 認識率を求める
correct_count = 0  # 正しく認識した回数
for n in range(len(test_x)):
    # テストを行う
    M = len(test_x[0])
    h1 = np.array([0.0, 0.0])
    for j in range(len(h1)):
        for i in range(M):
            h1[j] += test_x[n][i] * w1[j][i]

    g1 = np.array([0.0, 0.0])
    for j in range(len(h1)):
        g1[j] = 1 / (1 + math.exp(-h1[j]))  # シグモイド関数
    g1 = np.hstack((g1, -1))

    N = len(y[0])
    h2 = np.zeros(N)
    for k in range(len(h2)):
        for j in range(len(g1)):
            h2[k] += g1[j] * w2[k][j]

    g2 = np.array([0.0, 0.0, 0.0])
    for k in range(len(h2)):
        g2[k] = 1 / (1 + math.exp(-h2[k]))  # シグモイド関数
    z = np.argmax(g2)

    if z == np.argmax(test_y[n]):
        correct_count += 1

print("認識率は", correct_count / len(test_x))