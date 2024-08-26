import pandas as pd
from sklearn import datasets
iris = datasets.load_iris()
df = pd.DataFrame(iris.data,columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])
df["class"] = iris.target
cov=df.iloc[:, 0:4].cov()
cor=df.iloc[:, 0:4].corr()
print("Covariance:\n",cov)
print("\nCorelation:\n",cor)
