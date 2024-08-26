import seaborn as sns
import matplotlib.pyplot as plt
# Load the Iris dataset
iris = sns.load_dataset("iris")
#univariate
sl = iris.groupby("species")["sepal_length"].mean()
plt.pie(sl,labels=sl.index,autopct='%1.1f%%', 
colors=sns.color_palette("Set3"))
plt.title("Composition of Mean Sepal Length by Species")
plt.show()
#Multivariate
#Reducing the dataset to count of 40
iris = sns.load_dataset("iris").head(40)
# Group data by species and calculate the mean of numeric variables
species_data = iris.groupby("species")[["sepal_length","sepal_width","petal_length","petal_width"]]
# Create a stacked bar chart
species_data.plot(kind="bar",stacked=True,colormap="Set3",figsize=(18, 10))
# Set labels and title
plt.title("Multivariate Composition of Iris Species")
plt.xlabel("Species")
plt.ylabel("Mean Value")
# Show the plot
plt.legend(title="Variables",loc="upper right")
plt.tight_layout()
plt.show()
