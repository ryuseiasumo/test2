import pandas
from  sklearn import datasets
from matplotlib import pyplot

iris = datasets.load_iris()
print(iris)


iris_df = pandas.DataFrame(iris.data, columns = iris.feature_names)

print(iris_df.head())
print(iris_df.sort_values('sepal length (cm)').head())

print(iris_df.shape)
print(iris_df.info())

print(iris_df.describe())
print("平均値:", iris_df["sepal width (cm)"].mean())

iris_df["sepal total length (cm)"] = iris_df["sepal length (cm)"] + iris_df["sepal width (cm)"]
print(iris_df["sepal total length (cm)"].head())

iris_df.plot(x = "sepal length (cm)", y = "sepal width (cm)", kind = "scatter")
pyplot.show()

pyplot.show(iris_df["sepal length (cm)"].hist())

