import numpy as np

x = np.array([[1], [0], [-1]])
A = np.array([[1, 1, 1], [100, 0, 0]])

print("input vector: \n", x)
print("matrix with size = {} \n".format(A.shape), A)
print("product: \n", np.dot(A, x))

A = np.array([[1,2], [2,-3], [-1,2]])
B = np.array([[1, 2, -1]])
print("matrix A with shape = {} \n".format(A.shape), A)
print("matrix B with shape = {} \n".format(B.shape), B)
print("matrix BA with shape = {} \n".format(np.matmul(B, A).shape), np.matmul(B,A))


A = np.array([[2,3], [-2, 1]])
B = np.array([[-2, 1],[2, 3]])
C = A + B

print(A)
print(B)
print(C)

A = np.array([[2, 3, 4, 5],[-5, -4 , -3, -2]])
print("matrix A with shape = {}\n".format(A.shape),A)
print("matrix A^T with shape = {}\n".format(A.T.shape),A.T)


