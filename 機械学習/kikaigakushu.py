from sklearn import datasets

iris = datasets.load_iris()
print(iris.data[:10])

print(iris.target)



from sklearn import svm

clf = svm.SVC()
clf.fit(iris.data[:-1],iris.target[:-1])
print(clf.predict(iris.data[-1:]),iris.target[-1:])



import numpy as np
from matplotlib import pyplot
x = np.arange(-5, 5 ,0.1)
y = np.sin(x)

print(x[:10],y[:10])
pyplot.plot(x,y)
pyplot.show()

pyplot.plot(x,y,"o")
pyplot.show()

