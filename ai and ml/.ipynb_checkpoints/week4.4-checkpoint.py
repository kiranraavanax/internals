import seaborn as sns
import matplotlib.pyplot as plt
import pandas as p
iris = p.read_csv("C:/Users/kiran/Documents/ai and ml/IRIS.csv")
# Set the figure size
plt.figure(figsize=(18, 10))
# Create grouped bar plots for sepal length, sepal width, petal length, and petal width by species
plt.subplot(2, 2, 1)
sns.barplot(x="species", y="sepal_length", data=iris, palette="Set3")
plt.title("Comparison of Sepal Length by Species")
plt.subplot(2, 2, 2)
sns.barplot(x="species", y="sepal_width", data=iris, palette="Set3")
plt.title("Comparison of Sepal Width by Species")
plt.subplot(2, 2, 3)
sns.barplot(x="species", y="petal_length", data=iris, palette="Set3")
plt.title("Comparison of Petal Length by Species")
plt.subplot(2, 2, 4)
sns.barplot(x="species", y="petal_width", data=iris, palette="Set3")
plt.title("Comparison of Petal Width by Species")
# Adjust layout
plt.tight_layout()
# Show the plot
plt.show()
