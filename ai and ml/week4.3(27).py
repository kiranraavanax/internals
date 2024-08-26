import seaborn as sns
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")
#Univariate
sepal_length_data = iris["sepal_length"]
plt.figure(figsize=(8,6))
sns.histplot(sepal_length_data, color="skyblue")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.title("Univariate Distribution of Sepal Length")
plt.show()
#Multivariate
# Create subplots for each numeric variable
fig,axes = plt.subplots(2,2,figsize=(12,8))
# Plot sepal length distribution by species
sns.boxplot(x="species", y="sepal_length", data=iris, ax=axes[0, 0])
axes[0, 0].set_title("Distribution of Sepal Length by Species")
# Plot sepal width distribution by species
sns.boxplot(x="species", y="sepal_width", data=iris, ax=axes[0, 1])
axes[0, 1].set_title("Distribution of Sepal Width by Species")
# Plot petal length distribution by species
sns.boxplot(x="species", y="petal_length", data=iris, ax=axes[1, 0])
axes[1, 0].set_title("Distribution of Petal Length by Species")
# Plot petal width distribution by species
sns.boxplot(x="species", y="petal_width", data=iris, ax=axes[1, 1])
axes[1,1].set_title("Distribution of Petal Width by Species")
plt.tight_layout()
plt.show()
