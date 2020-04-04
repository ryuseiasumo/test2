import numpy as np

x = np.array([1.1, 2.2, 3.3])
print(x, type(x))

x = np.array([[1.0],[2.0],[3.0]])
print(x, type(x), "shape = ", x.shape)

x = np.array([-1, 0, -1])
y = np.array([0, 1, 0])
print(x+y, type(x+y))
print(x-y, type(x-y))

#スカラー倍
x = np.array([1, 1, 3])
alpha = -0.01
print(alpha * x, type(alpha*x))


#ノルム
x = np.array([0, 1, -1])
print("L^2-ノルム：", np.linalg.norm(x, 2))
print("L^5-ノルム：", np.linalg.norm(x, 5))
print("L^10-ノルム：", np.linalg.norm(x,10))


x = np.array([0, 1, -1])
y = np.array([1, 0, 1])
print("inner product:", np.inner(x, y))





