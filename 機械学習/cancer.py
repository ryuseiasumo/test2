from sklearn.datasets import load_breast_cancer
import pandas as pd

sample = load_breast_cancer()
print("sampleの数：{}".format(len(sample.data)))
print("sampleの中身：{}".format(sample.data[0]))
print("各sampleの特徴量の数：{}".format(len(sample.data[0])))

print("targetの数：{}".format(len(sample.target)))
print("targetの中身：{}".format(sample.target[0:30]))
