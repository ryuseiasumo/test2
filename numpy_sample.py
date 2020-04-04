import numpy as np

a = np.array([1,2,3])

print(a)
print(a.shape)


b = np.array([[1, 2, 3],[4, 5, 6]])

print(b)
print(b.shape)

zero = np.zeros((3,3))
print(zero)

tani = np.eye(3)
print(tani)

one = np.ones((3,3))
print(one)

ran = np.random.random((3,3))
print(ran)

a = np.array([[1,2,3],[4, 5, 6]])
b = np.array([[1,2,3],[4, 5, 6]])

print(a + b)
print(a * b)
print(np.dot(a, b.T))