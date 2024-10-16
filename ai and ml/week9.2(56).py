import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets 
from sklearn.decomposition import PCA

iris=datasets.load_iris()
x=iris.data
y=iris.target
print("feature shape:",x.shape) 
print("target shape:",y.shape)

pca=PCA(n_components=2)
pca.fit(x)
print("PCA Components:\n",pca.components_)

x=pca.transform(x) 
print("Transformed feture shape:",x.shape)


# Scatter plot of the 2D data
plt.figure(figsize=(8, 6))
plt.scatter(x[:, 0], x[:, 1], c=y, cmap='viridis', edgecolor='k', s=100)
plt.title('PCA of Iris Dataset')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar()
plt.show()

# Split the data into training and test sets (with random_state for reproducibility)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train a decision tree classifier
res = DecisionTreeClassifier()
res.fit(x_train, y_train)

# Predict on test data and evaluate accuracy
y_predict = res.predict(x_test)
accuracy = accuracy_score(y_test, y_predict)
