# %matplotlib inline  ←jupyternotebookでは必要
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs

X ,y = make_blobs(n_samples = 1000, centers = 5,n_features = 2,random_state = 0)

def normalize(x):
    min = x.min()
    max = x.max()
    result = (100 * (x-min)/(max-min)).astype(np.int64)
    return result

X = normalize(X[:,])
print("X shape:{}".format(X.shape))
print("X: {}".format(X))

from sklearn.cluster import KMeans
y_pred = KMeans(n_clusters = 2, random_state = 0).fit_predict(X)

plt.scatter(X[:, 0],X[: ,1], c=y_pred)
plt.show()

print(y_pred[0:3])
print(y_pred[999])

print("ラベル0の人数：{}".format(len(np.where(y_pred==1)[0])))
print("ラベル1の人数：{}".format(len(np.where(y_pred==0)[0])))


y_pred = KMeans(n_clusters = 5, random_state = 0).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c= y_pred)
plt.show()