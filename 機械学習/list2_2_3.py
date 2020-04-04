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
import numpy as np

def normalize(x):
    min = x.min()
    max = x.max()

    result = (10 * (x-min)/(max-min)).astype(np.int64)
    return result

dummy_x = x[:,[0, 6, 27]]
dummy_y = y
dummy_x[:,0] = normalize(dummy_x[:,0])
dummy_x[:,1] = normalize(dummy_x[:,1])
dummy_x[:,2] = normalize(dummy_x[:,2])

from sklearn.model_selection import ShuffleSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

ss = ShuffleSplit(n_splits = 1, random_state = 0, test_size=0.5, train_size=0.5)
train_index,test_index = next(ss.split(dummy_x))
x_train = dummy_x[train_index]
y_train = dummy_y[train_index]
x_test = dummy_x[test_index]
y_test = dummy_y[test_index]

clf = DecisionTreeClassifier(max_depth = 3)
clf = clf.fit(x_train, y_train)
predicted = clf.predict(x_test)
score = accuracy_score(predicted, y_test)

from sklearn import tree
import pydotplus
tree.export_graphviz(clf,out_file='dummy_tree.dot')

print(score)

from PIL import Image
dot_file_name = "./dummy_tree.dot"
png_file_name = "./dummy_tree.png"
graph = pydotplus.graph_from_dot_file(dot_file_name)
graph.write_png(png_file_name)
img =Image.open(png_file_name)
img.show()