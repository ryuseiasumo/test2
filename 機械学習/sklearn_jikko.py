from sklearn.datasets import load_breast_cancer
import pandas as pd

sample = load_breast_cancer()
print("sampleの数：{}".format(len(sample.data)))
print("sampleの中身：{}".format(sample.data[0]))
print("各sampleの特徴量の数：{}".format(len(sample.data[0])))

print("targetの数：{}".format(len(sample.target)))
print("targetの中身：{}".format(sample.target[0:30]))

from sklearn.svm import SVC
clf = SVC(kernel = "linear")

x = sample.data
y = sample.target

from sklearn.model_selection import ShuffleSplit
ss = ShuffleSplit(n_splits = 1, random_state = 0, test_size = 0.5, train_size = 0.5)

train_index, test_index = next(ss.split(x))
x_train = x[train_index]
y_train = y[train_index]
x_test = x[test_index]
y_test = y[test_index]

clf.fit(x_train,y_train)

print(clf.score(x_test,y_test))

